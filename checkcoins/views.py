from django.views.generic import TemplateView, ListView, FormView


class List(TemplateView):
    template_name = 'checkcoins/list.html'
