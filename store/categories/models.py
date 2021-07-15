from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, allow_unicode=True, unique=True)

    def __str__(self):
        return self.category_name


class Film(models.Model):
    film_name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    film = models.FileField(upload_to='films/')
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    def __str__(self):
        return self.film_name


class Member(User):
    self_desc = models.TextField(max_length=1000, blank=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

