from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User as AuthUser
from rest_framework.permissions import IsAuthenticated
from ..models import *
from ..serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'category_id'
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

class GameListAPIView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Game.objects.all()
    lookup_url_kwarg = 'category_id'
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)

    def get_games(self, category_id):
        try:
            return Game.objects.filter(category_id=category_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        company_id = kwargs.get('category_id')
        self.queryset = self.get_games(company_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GameDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    lookup_url_kwarg = 'game_id'
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)

class AllReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class AllNewsListAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class UserNewsListAPIView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = News.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

    def get_news(self, user_id):
        try:
            return News.objects.filter(user_id=user_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        self.queryset = self.get_news(user_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    lookup_url_kwarg = 'news_id'
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


class UserReviewListAPIView(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = Review.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_reviews(self, user_id):
        try:
            return Review.objects.filter(user_id=user_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        self.queryset = self.get_reviews(user_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    lookup_url_kwarg = 'review_id'
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)


# MESSAGES
class MessageListAPIView(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Message.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_messages(self, user_id):
        try:
            return Message.objects.filter(user_id=user_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        self.queryset = self.get_messages(user_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    lookup_url_kwarg = 'message_id'
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


# CARDS
class CardAPIView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Card.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = CardSerializer

    def get_card(self, user_id):
        try:
            return Card.objects.filter(user_id=user_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        self.queryset = self.get_card(user_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    lookup_url_kwarg = 'card_id'
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)


# CARTS
class CartAPIView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Cart.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_cart(self, user_id):
        try:
            return Cart.objects.filter(user_id=user_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        self.queryset = self.get_cart(user_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    lookup_url_kwarg = 'cart_id'
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)


# GAMEBOXES
class GameBoxAPIView(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = GameBox.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = GameBoxSerializer

    def get_game_box(self, user_id):
        try:
            return GameBox.objects.filter(user_id=user_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        self.queryset = self.get_game_box(user_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GameBoxDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameBox.objects.all()
    lookup_url_kwarg = 'game_box_id'
    serializer_class = GameBoxSerializer
    permission_classes = (IsAuthenticated,)


# LIST OF GAMES IN THE USER'S BOX
class UserGamesListAPIView(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    queryset = Game.objects.all()
    lookup_url_kwarg = 'box_id'
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)

    def get_games(self, box_id):
        list_of_games = []
        box = GameBox.objects.get(id=box_id)
        boxes_and_games = BoxesAndGames.objects.filter(box=box)

        for box in boxes_and_games:
            game = Game.objects.get(id=box.game.id)
            list_of_games.append(game)
        return list_of_games

    def get(self, request, *args, **kwargs):
        box_id = kwargs.get('box_id')
        self.queryset = self.get_games(box_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# BOXESANDGAMES
class BoxesAndGamesListAPIView(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    queryset = BoxesAndGames.objects.all()
    lookup_url_kwarg = 'game_box_id'
    serializer_class = BoxesAndGamesSerializer
    permission_classes = (IsAuthenticated,)

    def get_boxes_and_games(self, game_box_id):
        try:
            box = GameBox.objects.get(id=game_box_id)
            return BoxesAndGames.objects.filter(box=box)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        game_box_id = kwargs.get('game_box_id')
        self.queryset = self.get_boxes_and_games(game_box_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# LIST OF GAMES IN THE USER'S CART
class CartGamesListAPIView(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    queryset = Game.objects.all()
    lookup_url_kwarg = 'cart_id'
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)

    def get_games(self, cart_id):
        list_of_games = []
        cart = Cart.objects.get(id=cart_id)
        carts_and_games = CartsAndGames.objects.filter(cart=cart)

        for cart in carts_and_games:
            game = Game.objects.get(id=cart.game.id)
            list_of_games.append(game)
        return list_of_games

    def get(self, request, *args, **kwargs):
        cart_id = kwargs.get('cart_id')
        self.queryset = self.get_games(cart_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# CARTSANDGAMES
class CartsAndGamesListAPIView(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    queryset = CartsAndGames.objects.all()
    lookup_url_kwarg = 'game_cart_id'
    serializer_class = CartsAndGamesSerializer
    permission_classes = (IsAuthenticated,)

    def get_carts_and_games(self, game_cart_id):
        try:
            cart = GameBox.objects.get(id=game_cart_id)
            return BoxesAndGames.objects.filter(cart=cart)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        game_cart_id = kwargs.get('game_cart_id')
        self.queryset = self.get_boxes_and_games(game_cart_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#AUTH UUSERS

class AuthUserListAPIView(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = UserAuthSerializer

class AuthUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthUser.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = UserAuthSerializer
    permission_classes = (IsAuthenticated,)

class GetAuthUserAPIView(APIView):
    def get_user(self, username):
        try:
            return AuthUser.objects.get(username=username)
        except Exception as e:
            return Response({'error': str(e)})

    def get(self, request, username):
        user = self.get_user(username)
        serializer = UserAuthSerializer(user, many = False)
        return Response(serializer.data)


class GameBoxDetAPIView(APIView):
    def get_box(self, user_id):
        user = AuthUser.objects.get(id=user_id)
        try:
            return GameBox.objects.get(user=user)
        except Exception as e:
            return Response({'error': str(e)})

    def get(self, request, user_id):
        box = self.get_box(user_id)
        serializer = GameBoxSerializer(box, many = False)
        return Response(serializer.data)