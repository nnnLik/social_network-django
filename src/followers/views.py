from rest_framework import generics, permissions, views, response
from .models import Follower
from .serializers import UserFollowerSerializer

from src.profiles.models import UserSonet

class ListFollowerView(generics.ListAPIView):
    """Display a list of user Follower"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class=UserFollowerSerializer
    
    def get_queryset(self):
        return Follower.objects.filter(self.request.user)


class AddFollowerView(views.APIView):
    """Add a new Follower"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = UserSonet.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(subscriber=request.user)
            return response.Response(status=201)
        return response.Response(status=404)

    def delete(self, request, pk):
        try:
            subcriber = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        subcriber.delete()
        return response.Response(status=204)

