from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, allow_unicode=True, unique=True)

    def __str__(self):
        return self.cat_name


class Game(models.Model):
    game_name = models.CharField(max_length=150)
    description = models.TextField(max_length=600, blank=True, null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)

    def __str__(self):
        return self.game_name
