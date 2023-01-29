from .models import Chat, Room
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


"""
This function creates a new message in the database. It first gets the room object by filtering on the room_id,
then it gets the user and subscriber objects by filtering on the username,
and finally it creates a new Chat object with the user, subscriber, room_id, and text.
"""
@sync_to_async
def create_new_message(me, subscriber, message,room_id):
    get_room = Room.objects.filter(room_id=room_id)[0]
    user = User.objects.filter(username=user)[0]
    subscriber = User.objects.filter(username=subscriber)[0]
    Chat.objects.create(
        user=user,
        subscriber=subscriber,
        room_id=get_room,
        text=message)

class ChatRoom(AsyncWebsocketConsumer):

    """
    Connect:
    This function is called when the websocket is handshaking as part of the connection process.
    It adds the current channel to the room_group and accepts the connection.
    """
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    """
    Disconnect:
    This function is called when the websocket closes. It removes the current channel from the room_group
    """
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    """
    Receive:
    This function is called when the server receives a message. It first loads the json data,
    then it sends the message, username, and user_image to the group.
    """
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        user_image = text_data_json['user_image']

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
                'user_image': user_image,
            }
        )



    """
    Messages:
    This function is called when a message is received by the group. It first calls the create_new_message function
    to create a new message in the database, then it sends the message.
    """
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        user_image = event['user_image']

        # Create a new message in the database
        await create_new_message(user=self.scope["user"], subscriber=username, message=message, room_id=self.room_name)
        
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'user_image': user_image,
        }))