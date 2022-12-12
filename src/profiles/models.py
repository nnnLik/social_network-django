from django.db import models
from django.contrib.auth.models import AbstractUser


class UserSonet(AbstractUser):
    """User model for sonet"""

    first_login = models.DateTimeField('First login date', null=True,)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/')
