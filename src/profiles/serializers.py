from .models import UserSonet

from rest_framework import serializers


class GetUserSonetSerializer(serializers.ModelSerializer):
    """
    Filtered display user information
    """
    avatar = serializers.ImageField(write_only=True)
    class Meta:
        model = UserSonet
        exclude = (
            'password',
            'first_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions')


class GetUserSonetPublicSerializer(serializers.ModelSerializer):
    """
    Filtered display user information for public
    """
    class Meta:
        model = UserSonet
        exclude = (
            'email',
            'phone',
            'password',
            'first_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions')


class UserFollowerSerializer(serializers.ModelSerializer):
    """Serializer for Follower"""

    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = UserSonet
        fields = ('id', 'username', 'avatar')
