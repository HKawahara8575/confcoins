from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


# ログイン機能
class Login(FormView):
    template_name = 'checkcoins/login.html'

    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'checkcoins/login.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'checkcoins/login.html', {'form': form, })
