from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from .models import *
from .forms import *

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            users = User.objects.exclude(username=request.user.username) 
            return render(request, "index.html", {"users": users})
    else:
        form = SignupForm()  

    return render(request, "signup.html", {"form": form})


def login_view(request):
    form = LoginForm()
    error = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                users = User.objects.exclude(username=request.user.username) 
                return render(request, "index.html", {"users": users})
            else:
                error = "Invalid credentials."

    return render(request, "login.html", {"form": form, "error": error})

@login_required
def logout_view(request):
    logout(request)
    return redirect("chat:login")


@login_required
def chat_view(request):
    users = User.objects.exclude(username=request.user.username)  
    return render(request, "index.html", {"users": users})


@login_required
def chat_history(request, username):
    try:
        other_user = User.objects.get(username=username)
        messages = Message.objects.filter(
            sender__in=[request.user, other_user],
            receiver__in=[request.user, other_user]
        ).order_by("timestamp")
        messages_data = [
            {"sender": message.sender.username, "content": message.content, "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S")}
            for message in messages
        ]
        return JsonResponse({"messages": messages_data}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)

@login_required
def get_messages(request, username):
    try:
        other_user = User.objects.get(username=username)
        messages = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=other_user)) |
            (Q(sender=other_user) & Q(receiver=request.user))
        ).order_by('timestamp')
        
        # Format messages for the frontend
        message_list = [
            {'sender': msg.sender.username, 'text': msg.text, 'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
            for msg in messages
        ]
        return JsonResponse({'messages': message_list}, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=404)

@login_required
@csrf_exempt
def send_message(request, username):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            other_user = User.objects.get(username=username)
            text = data.get('text', '').strip()

            if text:
                Message.objects.create(sender=request.user, receiver=other_user, text=text)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'error': 'Empty message'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    