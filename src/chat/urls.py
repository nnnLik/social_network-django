from django.urls import re_path

from . import services

websocket_urlpatterns = [
        re_path(r'chat/(?P<chat_id>\w+)/$', services.ChatConsumer)
]