# from s5venv import create

from rest_framework import serializers
from unicodedata import category

from fresh_app.models import Category, Event, Favourite, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'event', 'content', 'created_at']


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ['id', 'user', 'event']


class EventSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    favourites = FavouriteSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'context', 'is_free', 'price', 'date', 'category', 'user', 'comments',
                  'favourites']

    # def validate(self, data):
    #     if data.get('is_free') and data.get('price') is not None:
    #         raise serializers.ValidationError("Price must be null for free events.")
    #     if not data.get('is_free') and data.get('price') is None:
    #         raise serializers.ValidationError("Price must be set for paid events.")
    #     return data

    def create(self, validated_data):
        event = Event(**validated_data)
        if event.is_free:
            event.is_free=True
        else:
            event.price = validated_data['price']
        event.save()
        return event


