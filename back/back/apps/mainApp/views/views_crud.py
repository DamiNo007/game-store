import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User as AuthUser
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import *
from datetime import datetime

@csrf_exempt
def categories_list(request):
    if request.method == 'GET':
        categories_list = Category.objects.order_by('id')
        categories_list_json = [category.short() for category in categories_list]
        return JsonResponse(categories_list_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        category = Category.objects.create(name=request_body.get('name', 'Category name is unknown'),
                                           img=request_body.get('img', 'No img'))
        return JsonResponse(category.short())


@csrf_exempt
def category_details(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(category.short())

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        category.name = request_body.get('name', category.name)
        category.img = request_body.get('img', category.img)
        category.save()
        return JsonResponse(category.short())

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def category_games(request, category_id):
    if request.method == 'GET':
        category_games = Game.objects.filter(category_id=category_id)
        category_games_json = [game.short() for game in category_games]
        return JsonResponse(category_games_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        game = Game.objects.create(full_name=request_body.get('full_name', 'No full name'),
                                   short_name=request_body.get('short_name', 'No short name'),
                                   price=request_body.get('price ', 0.0),
                                   genre=request_body.get('genre', 'No genre'),
                                   developer=request_body.get('developer', 'No developer'),
                                   publisher=request_body.get('publisher', 'No publisher'),
                                   release_date=request_body.get('release_date', "2000-01-01"),
                                   rating=request_body.get('rating', 0.0),
                                   description=request_body.get('description', 'No description'),
                                   img_path=request_body.get('img_path', 'No img path'),
                                   video_path=request_body.get('video_path', 'No video path'),
                                   sys_req=request_body.get('sys_req', 'No sys req'),
                                   min_sys_req=request_body.get('min_sys_req', 'No min sys req'),
                                   category_id=category_id)
        return JsonResponse(game.short(), safe=False)


@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users_list = User.objects.order_by('id')
        users_list_json = [user.short() for user in users_list]
        return JsonResponse(users_list_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        user = User.objects.create(first_name=request_body.get('first_name'),
                                   last_name=request_body.get('last_name'),
                                   email=request_body.get('email'),
                                   password=request_body.get('password'))
        return JsonResponse(user.short())


@csrf_exempt
def user_details(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(user.short())

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        user.first_name = request_body.get('first_name', user.first_name)
        user.last_name = request_body.get('last_name', user.last_name)
        user.email = request_body.get('email', user.email)
        user.password = request_body.get('password', user.password)
        user.save()
        return JsonResponse(user.short())

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def users_news(request, user_id):
    if request.method == 'GET':
        users_news = News.objects.filter(user_id=user_id)
        users_news_json = [news.short() for news in users_news]
        return JsonResponse(users_news_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        news = News.objects.create(news_photo=request_body.get('news_photo', 'No news photo'),
                                   news_name=request_body.get('news_name', 'No news name'),
                                   date=request_body.get('date ', "2000-01-01"),
                                   description=request_body.get('description', 'No description'),
                                   user_id=user_id)
        return JsonResponse(news.short(), safe=False)


@csrf_exempt
def news_details(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(news.short())

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        news.news_photo = request_body.get('news_photo', news.news_photo)
        news.news_name = request_body.get('news_name', news.news_name)
        news.date = request_body.get('date', news.date)
        news.description = request_body.get('description', news.description)
        news.save()
        return JsonResponse(news.short())

    elif request.method == 'DELETE':
        news.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def users_reviews(request, user_id):
    if request.method == 'GET':
        users_reviews = Review.objects.filter(user_id=user_id)
        users_reviews_json = [review.short() for review in users_reviews]
        return JsonResponse(users_reviews_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        review = Review.objects.create(review_photo=request_body.get('review_photo', 'No review photo'),
                                       review_name=request_body.get('review_name', 'No review name'),
                                       date=request_body.get('date ', "2000-01-01"),
                                       description=request_body.get('description', 'No description'),
                                       video_path=request_body.get('video_path', 'No video path'),
                                       user_id=user_id)
        return JsonResponse(review.short(), safe=False)


@csrf_exempt
def review_details(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(review.short())

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        review.review_photo = request_body.get('review_photo', review.review_photo)
        review.review_name = request_body.get('review_name', review.review_name)
        review.date = request_body.get('date', review.date)
        review.description = request_body.get('description', review.description)
        review.video_path = request_body.get('video_path', review.video_path)
        review.save()
        return JsonResponse(review.short())

    elif request.method == 'DELETE':
        review.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def users_messages(request, user_id):
    if request.method == 'GET':
        users_messages = Message.objects.filter(user_id=user_id)
        users_messages_json = [message.short() for message in users_messages]
        return JsonResponse(users_messages_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        message = Message.objects.create(user_name=request_body.get('user_name', 'No user name'),
                                         user_email=request_body.get('user_email', 'No user email'),
                                         subject=request_body.get('subject', 'No subject'),
                                         content=request_body.get('content', 'No content'),
                                         user_id=user_id)
        return JsonResponse(message.short(), safe=False)


@csrf_exempt
def message_details(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(message.short())

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        message.user_name = request_body.get('user_name', message.user_name)
        message.user_email = request_body.get('user_email', message.user_email)
        message.subject = request_body.get('subject', message.subject)
        message.content = request_body.get('content', message.content)
        message.save()
        return JsonResponse(message.short())

    elif request.method == 'DELETE':
        message.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def users_card(request, user_id):
    if request.method == 'GET':
        users_card = Card.objects.filter(user_id=user_id)
        users_card_json = [card.short() for card in users_card]
        return JsonResponse(users_card_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        card = Card.objects.create(full_name=request_body.get('full_name', 'No full name'),
                                   card_number=request_body.get('card_number', 0),
                                   expiration_date=request_body.get('expiration_date', '2000-02-02'),
                                   money_amount=request_body.get('money_amount', 0),
                                   security_code=request_body.get('security_code', 0),
                                   user_id=user_id)
        return JsonResponse(card.short(), safe=False)


@csrf_exempt
def card_details(request, card_id):
    try:
        card = Card.objects.get(id=card_id)
    except Card.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(card.short())

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        card.full_name = request_body.get('full_name', card.full_name)
        card.card_number = request_body.get('card_number', card.card_number)
        card.expiration_date = request_body.get('expiration_date', card.expiration_date)
        card.money_amount = request_body.get('money_amount', card.money_amount)
        card.security_code = request_body.get('security_code', card.security_code)
        card.save()
        return JsonResponse(card.short())

    elif request.method == 'DELETE':
        card.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def users_cart(request, user_id):
    if request.method == 'GET':
        users_cart = Cart.objects.filter(user_id=user_id)
        users_cart_json = [cart.short() for cart in users_cart]
        return JsonResponse(users_cart_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        cart = Cart.objects.create(user_id=user_id)
        return JsonResponse(cart.short(), safe=False)


@csrf_exempt
def cart_details(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(cart.short())


@csrf_exempt
def users_game_box(request, user_id):
    if request.method == 'GET':
        users_game_box = GameBox.objects.filter(user_id=user_id)
        users_game_box_json = [game_box.short() for game_box in users_game_box]
        return JsonResponse(users_game_box_json, safe=False)


@csrf_exempt
def game_box_details(request, game_box_id):
    try:
        game_box = GameBox.objects.get(id=game_box_id)
    except GameBox.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(game_box.short())