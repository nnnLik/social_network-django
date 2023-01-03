from django.db import models
from django.conf import settings
from src.profiles.serializers import UserFollowerSerializer


class Follower(models.Model):
    """Follower model"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                            related_name='Follower')
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                            related_name='Followers')