from django.views.generic import TemplateView, ListView, FormView


class Login(TemplateView):
    template_name = 'accounts/login.html'
