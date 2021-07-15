from django.urls import path

from .views import Greeting, GameView, GameListView

urlpatterns = [
    path('', Greeting.as_view()),
    path('game-list', GameListView.as_view(), name='game'),
    path('<slug:slug>/<slug:slug_1>', GameView.as_view())
]
