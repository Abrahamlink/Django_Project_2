from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Film


class Categories(TemplateView):
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class CategoriesViewList(ListView):
    model = Category
    template_name = 'CatList.html'
    context_object_name = 'list'


def categoryView(request, slug_name):
    template = loader.get_template('category.html')
    category = Category.objects.get(slug=slug_name)
    filmList = Film.objects.filter(category=category)
    context = {'list': filmList}
    return HttpResponse(template.render(context, request))


class CategoryFilmsView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.filter(category=context['category'])
        return context


class FilmInfoView(DetailView):
    model = Film
    template_name = 'film.html'
    context_object_name = 'filminfo'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        return HttpResponse('text')
