from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Players, Fixtures, Transfernews, Profile, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm, CommentForm
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

def home(request):
	fixtures = Fixtures.objects.all()
	return render(request, 'home.html', {'fixtures': fixtures})

def players(request):
	players = Players.objects.all()
	return render(request, 'players.html', {'players': players})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/')
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})

@login_required
def transfer_targets(request):
    transfernews = Transfernews.objects.all()
    news = request.POST.get('transfer_id', False)
    form = CommentForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.instance.transfernews_id = news
        form.save()
        messages.success(request, f'Your comment has been added')
        return redirect(request.path_info)
    return render(request, 'transfernews.html', {'transfernews': transfernews, 'form': form})

def PlayerDetailView(request, player):
    player = get_object_or_404(Players, name=player)
    context = {'player' : player}
    return render(request, 'player_detail.html',  context)



