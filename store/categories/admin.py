from django.contrib import admin
from .models import Category, Film, Member


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name', )}


class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_name', 'category', 'slug')
    prepopulated_fields = {'slug': ('film_name', )}


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Member, MemberAdmin)
