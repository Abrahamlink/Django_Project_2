from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, allow_unicode=True, unique=True)

    def __str__(self):
        return self.category_name


class Film(models.Model):
    film_name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    def __str__(self):
        return self.film_name
