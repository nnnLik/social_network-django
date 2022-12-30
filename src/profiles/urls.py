from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserSonetView.as_view({
        'get': 'retrieve','put': 'update'})),
    path('<int:pk>/', views.UserSonetPublicView.as_view(
        {'get': 'retrieve'})),
]