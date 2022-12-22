from .models import UserSonet

from rest_framework import serializers


class GetUserSonetSerializer(serializers.ModelSerializer):
    """
    Filtered display user information
    """
    class Meta:
        model = UserSonet
        exclude = ('password', 'first_login', 'is_active', 'is_staff', 'is_superuser',)
