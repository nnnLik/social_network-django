from django.db import models

from django.conf import settings


class Room(models.Model):
    """
    A model representing a dialog room in the application.
    """
    room_id = models.AutoField(primary_key=True, help_text="Unique ID for the room.")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE, help_text="User associated with the room.")
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscriber', on_delete=models.CASCADE, help_text="Subscriber")
    created_date = models.DateTimeField(auto_now_add=True, help_text="Date and time when the room was created.")

    def __str__(self):
        return f"{self.room_id}-{self.user}-{self.subscriber}"


class Chat(models.Model):
    """
    A model representing a chat between a user and a subscribed user.
    """
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, help_text="Foreign key linking the chat to a room.")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender', help_text="User who sent the message.")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver', help_text="User who received the message.")
    message = models.TextField(max_length=1024, help_text="Content of the message.")
    created_date = models.DateTimeField(auto_now_add=True, help_text="Date and time when the message was created.")
    has_seen = models.BooleanField(default=False, help_text="Indicates whether the message has been seen by the receiver.")

    def __str__(self):
        return f'{self.id} -{self.date}'