from django.urls import path
from . import views
from django.contrib.auth.views import logout

app_name = 'checkcoins'
urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
]
