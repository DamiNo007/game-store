from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as AuthUser
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..serializers import *

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryDetail(APIView):
    def get_category(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, category_id):
        categories = self.get_category(category_id)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, category_id):
        categories = self.get_category(category_id)
        serializer = CategorySerializer(instance=categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, category_id):
        categories = self.get_category(category_id)
        categories.delete()
        return Response({'deleted': True}, status=status.HTTP_200_OK)

class CategoryGames(APIView):
    def get_games(self, category_id):
        return Game.objects.filter(category_id=category_id)

    def get(self, request, category_id):
        category_games = self.get_games(category_id)
        serializer = GameSerializer(category_games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserList(APIView):
    def get(self, request):
        user = AuthUser.objects.all()
        serializer = UserAuthSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserDetail(APIView):
    def get_user(self, user_id):
        try:
            return AuthUser.objects.get(id=user_id)
        except AuthUser.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, user_id):
        user = self.get_user(user_id)
        serializer = UserAuthSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user = self.get_user(user_id)
        serializer = UserAuthSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, user_id):
        user = self.get_user(user_id)
        user.delete()
        return Response({'deleted': True}, status=status.HTTP_200_OK)

class UserNews(APIView):
    def get_news(self, user_id):
        return News.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        user_news = self.get_news(user_id)
        serializer = NewsSerializer(user_news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NewsDetail(APIView):
    def get_news(self, news_id):
        try:
            return News.objects.get(id=news_id)
        except News.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, news_id):
        news = self.get_news(news_id)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, news_id):
        news = self.get_news(news_id)
        serializer = NewsSerializer(instance=news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, news_id):
        news = self.get_news(news_id)
        news.delete()
        return Response({'deleted': True}, status=status.HTTP_200_OK)

class UsersReviews(APIView):
    def get_user_reviews(self, user_id):
        return Review.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        user_reviews = self.get_user_reviews(user_id)
        serializer = ReviewSerializer(user_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReviewDetail(APIView):
    def get_review(self, review_id):
        try:
            return Review.objects.get(id=review_id)
        except Review.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, review_id):
        review = self.get_review(review_id)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, review_id):
        review = self.get_review(review_id)
        serializer = NewsSerializer(instance=review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, review_id):
        review = self.get_news(review_id)
        review.delete()
        return Response({'deleted': True}, status=status.HTTP_200_OK)

class UsersMessage(APIView):
    def get_user_message(self, user_id):
        return Message.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        user_messages = self.get_user_message(user_id)
        serializer = MessageSerializer(user_messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MessageDetail(APIView):
    def get_message_detail(self, message_id):
        try:
            return Message.objects.get(id=message_id)
        except Message.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, message_id):
        messages = self.get_message_detail(message_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, message_id):
        message = self.get_review(message_id)
        serializer = MessageSerializer(instance=message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, message_id):
        message = self.get_news(message_id)
        message.delete()
        return Response({'deleted': True}, status=status.HTTP_200_OK)

class UsersCard(APIView):
    def get_users_card(self, user_id):
        return Message.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        users_card = self.get_users_card(user_id)
        serializer = CardSerializer(users_card, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CardDetail(APIView):
    def get_card_detail(self, user_id, card_id):
        try:
            return Card.objects.get(id=card_id)
        except Card.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, card_id):
        card_detail = self.get_card_detail(card_id)
        serializer = CardSerializer(card_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, card_id):
        card_detail = self.get_card_detail(card_id)
        serializer = MessageSerializer(instance=card_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, card_id):
        card_detail = self.get_card_detail(card_id)
        card_detail.delete()
        return Response({'deleted': True}, status=status.HTTP_200_OK)

class UsersCart(APIView):
    def get_users_cart(self, user_id):
        return Message.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        users_cart = self.get_users_card(user_id)
        serializer = CartSerializer(users_cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CartDetail(APIView):
    def get_cart(self, cart_id):
        return Cart.objects.filter(cart_id=cart_id)

    def get(self, request, cart_id):
        carts = self.get_users_card(cart_id)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UsersGameBox(APIView):
    def get_users_game_box(self, user_id):
        return GameBox.objects.filter(user_id=user_id)

    def get(self, request, user_id):
        game_boxes = self.get_users_card(user_id)
        serializer = GameBoxSerializer(game_boxes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

