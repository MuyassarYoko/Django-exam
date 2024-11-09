from django.db.models import Q
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterAPIView, CurrentUserAPIView, UserListAPIView, UserDetailView, UpdateUserAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('current_user/', CurrentUserAPIView.as_view(), name='current_user'),
    path('get/', UserListAPIView.as_view(), name='user-list'),
    path('get/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('update_user/', UpdateUserAPIView.as_view(), name='update_user'),
]
