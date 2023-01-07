from rest_framework import serializers
from .models import Follower
from src.profiles.serializers import UserFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):
    """List of Follower"""

    subscriber = UserFollowerSerializer(many=True, read_only=True)
    class Meta:
        model = Follower
        fields = ('subscriber', )