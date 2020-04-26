from django.contrib.auth.models import User as AuthUser
from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField('name of the category', max_length=200)
    img = models.TextField('path to the image')

    def __str__(self):
        return self.name

    def short(self):
        return {
            'name': self.name,
            'img': self.img
        }

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Game(models.Model):
    full_name = models.CharField('full name', max_length=200)
    short_name = models.CharField('short name', max_length=200)
    price = models.FloatField('price')
    genre = models.CharField('genre', max_length=200)
    developer = models.CharField('developer', max_length = 200)
    publisher = models.CharField('publisher', max_length = 200)
    release_date = models.DateField('release date')
    rating = models.FloatField('rating')
    description = models.TextField('description')
    img_path = models.TextField('image path')
    video_path = models.TextField('video_path')
    os_min = models.TextField('Min OS', default="Min OS")
    processor_min = models.TextField('Min processor', default="Min processor")
    memory_min = models.TextField('Min memory', default="Min memory")
    graphics_min = models.TextField('Min graphics', default="Min graphics")
    space_min = models.TextField('Min space', default="Min Space")
    os_opt = models.TextField('Optimal OS', default='Optimal OS')
    processor_opt = models.TextField('Optimal processor', default='Optimal processor')
    memory_opt = models.TextField('Optimal memory', default='Optimal memory')
    graphics_opt = models.TextField('Optimal graphics', default='Optimal graphics')
    space_opt = models.TextField('Optimal space', default='Optimal space')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'games')

    def __str__(self):
        return self.full_name

    def short(self):
        return {
            'full_name':self.full_name,
            'short_name': self.short_name,
            'price': self.price,
            'genre': self.genre,
            'developer': self.developer,
            'publisher': self.publisher,
            'release_date': self.release_date,
            'rating': self.rating,
            'description': self.description,
            'img_path': self.img_path,
            'video_path': self.video_path,
            'sys_req': self.sys_req,
            'min_sys_req': self.min_sys_req,
            'category': self.category.name
        }

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

class News(models.Model):
    news_photo = models.TextField('News Photo')
    news_name = models.CharField('News Name', max_length=200)
    date = models.DateTimeField('Date')
    description = models.TextField('Description')
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.news_name

    def short(self):
        return {
            'Id': self.id,
            'News Name': self.news_name
        }

    def full(self):
        return {
            'Id': self.id,
            'News Photo': self.news_photo,
            'News Name': self.news_name,
            'Date': self.date,
            'Description': self.description
        }

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Newses(models.Model):
    news_photo = models.TextField('News Photo')
    news_name = models.CharField('News Name', max_length=200)
    date = models.DateTimeField('Date')
    description = models.TextField('Description')
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.news_name

    def short(self):
        return {
            'Id': self.id,
            'News Name': self.news_name
        }

    def full(self):
        return {
            'Id': self.id,
            'News Photo': self.news_photo,
            'News Name': self.news_name,
            'Date': self.date,
            'Description': self.description
        }

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Review(models.Model):
    review_photo = models.TextField('Review Photo')
    review_name = models.CharField('Review Name', max_length=200)
    date = models.DateTimeField('Date')
    description = models.TextField('Description')
    video_path = models.TextField('Video Path')
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name = 'reviews')

    def __str__(self):
        return self.review_name

    def short(self):
        return {
            'Id': self.id,
            'Review Name': self.review_name
        }

    def full(self):
        return {
            'Id': self.id,
            'Review Photo': self.review_photo,
            'Review Name': self.review_name,
            'Date': self.date,
            'Description': self.description,
            'Video Path': self.video_path
        }

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

class Cart(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)

    def str(self):
        return self.user

    def short(self):
        return {
            'Id': self.id,
            'User': self.user
        }

    class Meta:
        verbose_name = 'Cart'
        verbose_name = 'Carts'


class CartsAndGames(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def str(self):
        return self.cart_id

    def short(self):
        return {
            'Id': self.id,
            'Game ID': self.game,
            'Cart ID': self.cart
        }

    class Meta:
        verbose_name = 'CartsAndGames'
        verbose_name_plural = 'CartsAndGames'

class GameBox(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)

    def str(self):
        return self.user

    def short(self):
        return {
            'Id': self.id,
            'User': self.user
        }

    class Meta:
        verbose_name = "Box"
        verbose_name_plural = "Boxes"

class BoxesAndGames(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    box = models.ForeignKey(GameBox, on_delete=models.CASCADE)

    def short(self):
        return {
            'Id': self.id,
            'Game ID': self.game,
            'Cart ID': self.box
        }

    class Meta:
        verbose_name = 'BoxesAndGames'
        verbose_name_plural = 'BoxesAndGames'

class RuslansMessages(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_name='Ruslan')

class Message(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    user_name = models.CharField('User Name', max_length=200)
    user_email = models.CharField('Email', max_length=200)
    subject = models.CharField('Subject', max_length=200)
    content = models.TextField('Content')
    objects = models.Manager()
    ruslans_messages = RuslansMessages()

    def str(self):
        return self.user_name

    def short(self):
        return {
            'Id': self.id,
            'User Name': self.user_name,
            'User Email': self.user_email
        }

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

class Card(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    full_name = models.CharField('Full Name', max_length=200)
    card_number = models.IntegerField('Card Number')
    expiration_date = models.DateTimeField('Expiration Date')
    money_amount = models.FloatField('Money', max_length=20)
    security_code = models.IntegerField('Security Code')

    def str(self):
        return self.full_name

    def short(self):
        return {
            'Id': self.id,
            'Full Name': self.full_name,
            'Card Number': self.card_number
        }

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
