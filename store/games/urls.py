from django.urls import path

from store.games.views import Greeting

urlpatterns = [
    path('', Greeting.as_view())
]
