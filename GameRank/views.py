from logging import getLogger
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GameRank1, Profile
from .forms import GameRankForm, SingUpForm
LOGGER = getLogger()

# def gamerank_list(request):
#     ranking = GameRank1.objects.values('username','ranking')
#     return render(request, 'gamerank_list.html', {'rankinglist': ranking})

def gamerank_list(request):
    # for x in range(2):
    username = GameRank1.objects.values('username')
    rankingVal = GameRank1.objects.values('ranking')
        # # ranking = {"User":username, "ranking":rankingVal}
        # ranking = {username, rankingVal}
        # ranking = {GameRank1.objects.values('username'), GameRank1.objects.values('ranking')}
    return render(request, 'gamerank_list.html', {'rankinglist': rankingVal}, {'usernamelist': username})

def update_gamerank(request):
    Gr1Obj1 = GameRank1.objects.values('username')
    # Gr1Obj2 = GameRank1.objects.values('ranking')
    # Gr1Obj = {Gr1Obj1: Gr1Obj2}
    return render(request, 'gamerank_list.html', {'update_gamerank': Gr1Obj1})

class GameRankCreateView(CreateView):

    template_name = 'form.html'
    form_class = GameRankForm
    success_url = reverse_lazy('gamerank_create')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class GameRankUpdateView(UpdateView):

    template_name = 'form.html'
    model = GameRank1
    form_class = GameRankForm
    success_url = reverse_lazy('gamerank')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a GameRank.')
        return super().form_invalid(form)


class RankDeleteView(DeleteView):
    template_name = 'delete.html'
    model = GameRank1
    success_url = reverse_lazy('gamerank')


class GameRankListView(LoginRequiredMixin, ListView):
    template_name = 'gamerank_list.html'
    model = GameRank1

class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SingUpForm
    success_url = reverse_lazy('gamerank')

class GameRankView(LoginRequiredMixin, View):
   def get(self, request):
       print(request.username)
       profile = Profile.objects.get(user=request.username)
       if profile.clicks_left > 0:
           profile.clicks_left -= 1
           profile.save()
           return render(
               request, template_name='gamerank_list.html',
               context={'GameRank': GameRank1.objects.all()}
           )
       else:
           return render(request, template_name='no_clicks.html')


