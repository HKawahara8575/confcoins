from django.urls import path
from . import views

app_name = 'checkcoins'
urlpatterns = [
    path('list', views.List.as_view(), name='list'),
]
