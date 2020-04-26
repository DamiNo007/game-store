from django.urls import path
from .views.views_generic import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('categories/', CategoryListAPIView.as_view(), name="categories"),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name="category detail"),
    path('games/<int:game_id>/', GameDetailAPIView.as_view(), name="game details"),
    path('categories/<int:category_id>/games/', GameListAPIView.as_view(), name="games"),
    path('users/', AuthUserListAPIView.as_view(), name="users"),
    path('users/<int:user_id>/', AuthUserDetailAPIView.as_view(), name="user detail"),
    path('users/<str:username>/', GetAuthUserAPIView.as_view(), name="user detail"),
    path('users/<int:user_id>/news/', UserNewsListAPIView.as_view(), name="news"),
    path('news/<int:news_id>/', NewsDetailAPIView.as_view(), name="review detail"),
    path('users/<int:user_id>/reviews/', UserReviewListAPIView.as_view(), name="reviews"),
    path('reviews/<int:review_id>/', ReviewDetailAPIView.as_view(), name="review detail"),
    path('reviews/', AllReviewListAPIView.as_view(), name = "all reviews"),
    path('news/', AllNewsListAPIView.as_view(), name = "all news"),
    path('<int:user_id>/messages/', MessageListAPIView.as_view(), name="messages"),
    path('messages/<int:message_id>/', MessageDetailAPIView.as_view(), name="message detail"),
    path('<int:user_id>/card/', CardAPIView.as_view(), name= "card"),
    path('<int:user_id>/card/<int:card_id>/', CardDetailAPIView.as_view(), name="card detail"),
    path('<int:user_id>/cart/', CartAPIView.as_view(), name= "cart"),
    path('cart/<int:cart_id>/', CartDetailAPIView.as_view(), name="cart detail"),
    path('<int:user_id>/game_box/', GameBoxDetAPIView.as_view(), name="gamebox"),
    #path('game_box/<int:game_box_id>/', GameBoxDetailAPIView.as_view(), name="gamebox detail"),
    path('<int:user_id>/<int:cart_id>/games/', GameBoxDetailAPIView.as_view(), name="gamebox detail"),
    path('<int:box_id>/usergames/', UserGamesListAPIView.as_view(), name="games of the user"),
    path('<int:game_box_id>/boxes_and_games/', BoxesAndGamesListAPIView.as_view(), name="boxes and games"),
    path('<int:cart_id>/cartgames/', CartGamesListAPIView.as_view(), name="games in the cart"),
    path('<int:cart_id>/carts_and_games/', CartsAndGamesListAPIView.as_view(), name="boxes and games"),
]
