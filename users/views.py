from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import status, generics
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from yaml import serialize

from users.forms import RegistrationForm
from users.models import User
from users.serializers import UserSerializers, RegisterSerializers, UserUpdateSerializer


class CurrentUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_active:
            return Response({"detail": "User  is inactive."}, status=403)

        serializer = UserSerializers(request.user)
        return Response(serializer.data)


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_serializer = TokenObtainPairSerializer(data={
            'username': user.username,
            'password': request.data['password']  # Use the password provided in the request
        })
        token_serializer.is_valid(raise_exception=True)
        tokens = token_serializer.validated_data

        return Response({
            'user': {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name
            },
            'tokens': tokens
        }, status=status.HTTP_201_CREATED)



class UpdateUserAPIView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.filter(role='user')
    serializer_class = UserSerializers


class UserDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializers

    # def get_queryset(self):
    #     queryset = User.objects.all()
    #
    #     search_query = self.request.query_params.get('search', '')
    #     if search_query:
    #         queryset = queryset.filter(
    #             first_name__icontains=search_query
    #         ) | queryset.filter(
    #             last_name__icontains=search_query
    #         )
    #
    #     return queryset
    #
    # def get(self, request: Request, *args, **kwargs):
    #     page = int(request.query_params.get('page', 1))
    #     limit = int(request.query_params.get('limit', 5))
    #     if limit <= 0:
    #         limit = 5
    #     start_index = (page - 1) * limit
    #     end_index = start_index + limit
    #
    #     queryset = self.get_queryset()
    #     all_users = list(queryset)
    #     paginated_users = all_users[start_index:end_index]
    #
    #     serializer = self.get_serializer(paginated_users, many=True)
    #     response_data = {
    #         'result': serializer.data,
    #         'count': len(all_users),
    #         'page': page,
    #         'limit': limit
    #     }
    #
    #     return Response(response_data)

