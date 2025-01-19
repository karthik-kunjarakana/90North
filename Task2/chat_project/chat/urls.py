from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('signup/', views.signup_view, name='signup'),
    path('chat/', views.chat_view, name='chat'),  
    path('logout/', views.logout_view, name='logout'),
    path('get_messages/<str:username>/', views.get_messages, name='get_messages'),
    path('send_message/<str:username>/', views.send_message, name='send_message'),
]
