from django.urls import path
from .views import Categories, CategoriesViewList, CategoryFilmsView, FilmInfoView, addFilmView, FilmsList, \
    RegistrationView, MyLoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Categories.as_view(), name='categories'),
    path('cats', CategoriesViewList.as_view(), name='categoriesList'),
    path('cats/<slug:slug>', CategoryFilmsView.as_view(), name='FilmsList'),
    path('films/', FilmsList.as_view()),
    path('films/<slug:slug>', FilmInfoView.as_view(), name='FilmInfo'),
    path('addFilm', addFilmView, name='add'),
    path('reg', RegistrationView.as_view()),
    path('login', MyLoginView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
