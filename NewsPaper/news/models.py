from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from SHORTER import *


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        postR = self.post_set.all().aggregate(postRating=Sum('rating'))
        p_R = 0
        p_R += postR.get('postRating')

        commentR = self.authorUser.comment_set.all().aggregate(comment_rating=Sum('rating'))
        c_R = 0
        c_R += commentR.get('comment_rating')

        self.rating_author = p_R * 3 + c_R
        self.save()

    def __str__(self):
        return f"{self.authorUser}"


class Category(models.Model):
    name_category = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    PostNews = 'PN'
    PostArticle = 'PA'

    POSITIONS = [
        (PostArticle, 'Статья'),
        (PostNews, 'Новость'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_find = models.CharField(max_length=30, choices=Category_choises, default=Article)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField('Category', through='PostCategory')
    tittle = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    positions = models.CharField(max_length=2, choices=POSITIONS, default=PostArticle, verbose_name='Тип поста')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:128] + '...'

    def __str__(self):
        data = 'Post from {}'.format(self.date_of_creation.strftime('%d.%m.%Y %H:%M'))


class PostCategory(models.Model):
    post_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f"{self.comment_date}, {self.comment_user}"
