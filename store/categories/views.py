from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.defaultfilters import slugify

from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView
from .models import Category, Film, Member
from .forms import LoginForm

from django.contrib.auth import login, authenticate, logout


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


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


def addFilmView(request):
    template = loader.get_template('creating.html')
    context = {'genres': Category.objects.all()}

    if request.method == 'POST':
        film = Film(
            film_name=request.POST['film'],
            category=Category.objects.get(id=request.POST['genre']),
            film=request.POST['video'],
            slug=slugify(request.POST['film'])
        )
        film.save()
    return HttpResponse(template.render(context, request))


class FilmsList(ListView):
    model = Film
    context_object_name = 'list'
    template_name = 'films.html'


class RegistrationView(CreateView):
    template_name = 'registration.html'
    model = Member
    fields = [
        'username',
        'password',
        'email'
    ]
    success_url = '/'


class MyLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/cats'
    form_class = LoginForm

    def form_valid(self, form):
        form.login()
        # print(self.request)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
