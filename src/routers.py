from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from src.chat.urls import websocket_urlpatterns

schema_view = get_schema_view(
	openapi.Info(
		title="SoNet API",
		default_version='v1.0.0',
		description="social network api",
	),
	public=True,
	permission_classes=[permissions.AllowAny],
)

urlpatterns = [
	path('', include('src.profiles.urls')),
	path('wall/', include('src.wall.urls')),
	path('feed/', include('src.feed.urls')),
	path('follower/', include('src.followers.urls')),

	path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

application = ProtocolTypeRouter({
	'websocket': AuthMiddlewareStack(
		URLRouter(websocket_urlpatterns)
	)
})