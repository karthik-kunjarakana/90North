import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        messages = await self.load_messages(self.room_name)
        for message in messages:
            await self.send(json.dumps({
                "message": message["content"],
                "sender": message["sender"]
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data['message']

        receiver = await sync_to_async(User.objects.get)(username=self.room_name)
        message = await self.save_message(self.user, receiver, message_content)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message.content,
                'sender': self.user.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))

    @sync_to_async
    def save_message(self, sender, receiver, content):
        return Message.objects.create(sender=sender, receiver=receiver, content=content)

    @sync_to_async
    def load_messages(self, username):
        receiver = User.objects.get(username=username)
        messages = Message.objects.filter(
            sender__in=[self.user, receiver], receiver__in=[self.user, receiver]
        ).order_by('timestamp')
        return [{"content": message.content, "sender": message.sender.username} for message in messages]
