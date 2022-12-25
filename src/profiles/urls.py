from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.GetUserSonetView.as_view()),
    path('<int:pk>/', views.GetUserSonetView.as_view())
]