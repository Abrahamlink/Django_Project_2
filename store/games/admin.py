from django.contrib import admin

from .models import Category, Game


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug')
    prepopulated_fields = {'slug': ('cat_name', )}


class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'cat', 'description', 'slug')
    prepopulated_fields = {'slug': ('game_name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
