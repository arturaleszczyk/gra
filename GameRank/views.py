from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, world!')

import json
import os.path
import random
import string
from logging import getLogger

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Url, GameRank1, Profile
from .forms import GameRankForm, SingUpForm


LOGGER = getLogger()


def append_to_json(url, short_code):
    data = {}
    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            data = json.load(f)
    data[short_code] = url
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))


def redirects(request, short_code):
    url_obj = Url.objects.get(short_code=short_code)
    return redirect(url_obj.url)


def template_view(request):
    return render(
       request,
       template_name='hello.html',
       context={
           'adjectives':
               ['beautiful',
                'wonderful',
                'cruel',
                'awful'],
           'numbers': range(1, 11)
       }
    )


def gamerank_list(request):
    return render(
        request,
        template_name='gamerank_list.html',
        context={'gamerank': GameRank1.objects.all()}
    )


class GameRankCreateView(CreateView):

    template_name = 'form.html'
    form_class = GameRankForm
    success_url = reverse_lazy('movie_create')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class GameRankUpdateView(UpdateView):

    template_name = 'form.html'
    model = GameRank1
    form_class = GameRankForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)


class RankDeleteView(DeleteView):
    template_name = 'delete.html'
    model = GameRank1
    success_url = reverse_lazy('movies')


class GameRankListView(LoginRequiredMixin, ListView):
    template_name = 'movies_list.html'
    model = GameRank1

class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SingUpForm
    success_url = reverse_lazy('movies')

class GameRankView(LoginRequiredMixin, View):
   def get(self, request):
       print(request.user)
       profile = Profile.objects.get(user=request.user)
       if profile.clicks_left > 0:
           profile.clicks_left -= 1
           profile.save()
           return render(
               request, template_name='movies_list.html',
               context={'GameRank': GameRank1.objects.all()}
           )
       else:
           return render(request, template_name='no_clicks.html')