#from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect, reverse

from .models import Author
from .forms import AuthorForm


class IndexView(ListView):
        model = Author
        template_name = 'authors/index.html'
        context_object_name='authors'


        def get_queryset(self):
            queryset = super().get_queryset()
            print(queryset)
            queryset = queryset.filter(id__gt=1)
            print(queryset)
            return queryset

class CreateAuthorView(TemplateView):
    template_name = 'authors/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorForm
        return context

    def post(self, request):
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return render(request. self.template_name, {'form':form})
        
        new_author = form.save(commit=False)
        new_author.level = 'J'
        new_author.save()
        return redirect(reverse('authors:index'))

