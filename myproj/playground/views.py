from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Article


class IndexView(TemplateView):
    template_name = 'playground/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context
