from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>', views.AddFollowerView.as_view()),
    path('', views.ListFollowerView.as_view())
]