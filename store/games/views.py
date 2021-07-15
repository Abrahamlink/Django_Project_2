from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Game, Category


class Greeting(TemplateView):
    template_name = 'games/index.html'


class GameView(DetailView):
    model = Game
    template_name = 'games/game.html'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        context = {
            'game': Game.objects.filter(slug=kwargs['slug_1'])
        }
        print(context)
        return HttpResponse(render(request, self.template_name, context))


class GameListView(ListView):
    model = Game
    template_name = 'games/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_slugs = [x.slug for x in Category.objects.all()]
        game_slugs = [x.slug for x in Game.objects.all()]
        context['list'] = list(zip(Game.objects.all(), cat_slugs, game_slugs))
        return context

