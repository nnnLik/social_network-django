from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import GetUserSonetSerializer, GetUserSonetPublicSerializer

from .models import UserSonet


class UserSonetPublicView(ModelViewSet):
	"""Display user information for a public"""

	queryset = UserSonet.objects.all()
	serializer_class = GetUserSonetPublicSerializer
	permission_classes = [permissions.AllowAny]


class UserSonetView(ModelViewSet):
	"""Display user information"""

	serializer_class = GetUserSonetSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return UserSonet.objects.filter(id=self.request.user.id)
