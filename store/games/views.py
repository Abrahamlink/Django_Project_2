from django.shortcuts import render
from django.views.generic import TemplateView


class Greeting(TemplateView):
    template_name = 'games/index.html'
