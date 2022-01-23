from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# ログイン
def login_(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            # ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request, user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('checkcoins:home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'accounts/login.html')


# ログアウト
@login_required
def logout_(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('accounts:login'))

