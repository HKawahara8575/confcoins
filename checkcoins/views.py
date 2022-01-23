from django.views.generic import TemplateView, ListView, FormView


class List(ListView):
    template_name = 'checkcoins/list.html'
