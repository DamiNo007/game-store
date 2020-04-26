from django.contrib.auth.models import User as AuthUser
from rest_framework import serializers
from .models import *
import datetime

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    img = serializers.CharField()

    def create(self, validated_data):
        category = Category()
        category.name = validated_data.get('name', 'No name')
        category.img = validated_data.get('img', 'No image')
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.img = validated_data.get('img', instance.img)
        instance.save()

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.CharField()
#     password = serializers.CharField()
#
#     def create(self, validated_data):
#         user = User()
#         user.first_name = validated_data.get('first_name', 'No name')
#         user.last_name = validated_data.get('last_name', 'No lastname')
#         user.email = validated_data.get('email', 'No email')
#         user.password = validated_data.get('password', 'No password')
#         user.save()
#         return user
#
#     def update(self, instance, validated_data):
#         instance.fisrt_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.save()
#         return instance

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class GameBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameBox
        fields = '__all__'

class CartsAndGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartsAndGames
        fields = '__all__'

class BoxesAndGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxesAndGames
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
