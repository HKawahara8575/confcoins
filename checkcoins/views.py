from django.views.generic import TemplateView, ListView, FormView


class Home(TemplateView):
    template_name = 'checkcoins/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["UserID"] = self.request.user
        return context

