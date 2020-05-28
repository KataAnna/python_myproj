from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


from datetime import datetime, timedelta
from random import randint


class ArticleView(TemplateView):

    template_name = 'homepage/articles.html'

    def get_dates_list(self, count=10):
        result = []
        today = datetime.today() - timedelta(days=7)
        for i in range(count):
            date = today - timedelta(days=i)
            for j in range(randint(1, 4)):
                result.append(date.replace(hour=randint(0, 23)))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        my_obj = MyClass()
        my_obj.data = {'spam' : 'eggs'}
        my_obj.list = list(range(10, 20))
        args={
            'articles': list(range(1, 6)),
            'val0':'1hi',
            'val1': 'OTUS',
            'val2': False,
            'obj': my_obj,
            'a_title':'djaNgo and subLine text 3',
            'string': ('First line\n'
                        'Second line\n'
                        'Third line\n'
                        ),
            'current': datetime.today(),
            'dates': self.get_dates_list(),
        }
        context.update(args)
        return context

    
def article_year(request, year):
    return HttpResponse(f'<h1>Year is {year} <h1>')

class MyClass():
    foo = 42

    def __repr__(self):
        return f'<MyClass{self.foo}>'
