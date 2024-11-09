import datetime

from django.db.models import Q
from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from yaml import serialize

from fresh_app.models import Event, Category, Comment, Favourite
from fresh_app.pagination import MyPagination
from fresh_app.serializers import EventSerializer, CategorySerializer, CommentSerializer, FavouriteSerializer


class EventList(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = MyPagination

    # def get(self, request):
    #     events = Event.objects.all()
    #     paginator = self.pagination_class()
    #     paginated_events = paginator.paginate_queryset(events, request)
    #     title = request.query_params.get('title', None)
    #     if title:
    #         events = events.filter(title__icontains=title)
    #     serializer = EventSerializer(paginated_events, many=True)
    #     return paginator.get_paginated_response(serializer.data)


class EventCreate(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventDetail(RetrieveAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventUpdate(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDelete(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CategoryList(ListAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # pagination_class = MyPagination

    # def get(self, request):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, many=True)
    #     return Response(serializer.data)


class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDelete(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentList(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = MyPagination


class CommentDUD(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = MyPagination


class FavouriteList(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class FavouriteDUD(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
