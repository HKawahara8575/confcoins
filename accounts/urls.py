from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.login_, name='login'),
    path('logout', views.logout_, name='logout')
]