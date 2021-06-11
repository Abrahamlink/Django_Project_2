from django.urls import path
from .views import Categories, CategoriesViewList, CategoryFilmsView, FilmInfoView


urlpatterns = [
    path('', Categories.as_view(), name='categories'),
    path('cats', CategoriesViewList.as_view(), name='categoriesList'),
    path('cats/<slug:slug>', CategoryFilmsView.as_view(), name='FilmsList'),
    path('films/<slug:slug>', FilmInfoView.as_view(), name='FilmInfo')
]
