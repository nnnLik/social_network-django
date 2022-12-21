from random import choices

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserSonet(AbstractUser):
    """User model for sonet"""

    GENDER = (
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    )

    avatar = models.ImageField(upload_to='user/avatar/')

    first_login = models.DateTimeField('First login date', blank=True, null=True)
    birthday = models.DateTimeField('Birthday date', blank=True, null=True)
    gender  = models.CharField('Gender', max_length=6, choices=GENDER)

    phone = models.CharField('Phone number', max_length=14)
    biography = models.TextField('User Biography', blank=True, null=True)

    github = models.CharField('User GitHub', max_length=500, blank=True, null=True)
    linkedin = models.CharField('User Linkedin', max_length=500, blank=True, null=True)

    work_place = models.CharField('User Work Place', max_length=150, blank=True, null=True)
    work_position = models.CharField('User Work Position', max_length=150, blank=True, null=True)
