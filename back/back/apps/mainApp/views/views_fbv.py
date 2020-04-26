from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User as AuthUser
from ..models import Category, Game, News, Review, Cart, CartsAndGames, GameBox, BoxesAndGames, Message, Card
from ..serializers import *

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        category.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def category_games(request, category_id):
    try:
        games = Game.objects.filter(category_id=category_id)
    except Game.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        user = AuthUser.objects.all()
        serializer = UserAuthSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def user_detail(request, user_id):
    try:
        user = AuthUser.objects.get(id=user_id)
    except AuthUser.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = UserAuthSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserAuthSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        user.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def users_news(request, user_id):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def news_detail(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NewsSerializer(instance=news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        news.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def users_reviews(request, user_id):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def review_detail(request, review_id):
    try:
        reviews = Review.objects.get(id=review_id)
    except Review.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance=reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        reviews.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def users_message(request, user_id):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def message_detail(request, message_id):
    try:
        messages = Message.objects.get(id=message_id)
    except Message.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = MessageSerializer(messages)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MessageSerializer(instance=messages, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        messages.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def users_card(request, user_id):
    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def card_detail(request, user_id, card_id):
    try:
        cards = Card.objects.get(id=card_id)
    except Card.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CardSerializer(cards)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CardSerializer(instance=cards, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        cards.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def users_cart(request, user_id):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def cart_detail(request, cart_id):
    try:
        carts = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CartSerializer(carts)
        return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def users_game_box(request, user_id):
    if request.method == 'GET':
        game_boxes = GameBox.objects.all()
        serializer = GameBoxSerializer(game_boxes, many=True)
        return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def game_box_detail(request, user_id, cart_id):
    try:
        game_boxes = GameBox.objects.get(id=cart_id)
    except GameBox.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = GameBoxSerializer(game_boxes)
        return Response(serializer.data)

