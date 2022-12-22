from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions

from .models import UserSonet
from .serializers import GetUserSonetSerializer


class GetUserSonetView(RetrieveAPIView):
	"""Display user information"""

	queryset = UserSonet.objects.all()
	serializer_class = GetUserSonetSerializer


class UpdateUserSonetView(UpdateAPIView):
	"""Edit user information"""

	serializer_class = GetUserSonetSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return UserSonet.objects.filter(id=self.request.user.id)
