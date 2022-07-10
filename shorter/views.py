from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm, ShorterHistoryForm
from random import randint
from django.contrib.auth.models import User
from .models import Shorter_history

def url_shortener():
    base_list = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    short_url = ''
    for x in range(0,6):
        short_url += base_list[randint(0,61)]
    return short_url

def index(request):
    if request.method == 'POST':
        user = request.user
        user_url = request.POST['user_url']
        if len(user_url) > 6:
            while True:
                short_url = url_shortener()
                try:
                    Shorter_history.objects.get(short_url=short_url)
                except:
                    Shorter_history.objects.create(user_id=user, user_url=user_url, short_url=short_url)
                    return render(request, 'index.html', {'short_url' : short_url, 'user_url': user_url,})
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('/')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form':form,})

def user_shorter_history(request):
    user = request.user
    shorters = Shorter_history.objects.filter(user_id=user)
    return render(request, 'history.html', {'shorters':shorters,})

def redirect_short_url(request, short_url):
    shorter_object = Shorter_history.objects.get(short_url=short_url)
    return redirect(shorter_object.user_url)
