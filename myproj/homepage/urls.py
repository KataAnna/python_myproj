from django.urls import path, register_converter
from django.views.generic import TemplateView

from . import views

app_name = 'homepage'

class YearConvertor:
    regex = r'[0-9]{4}'

    def to_python(self, value):
        value = int(value)
        if value < 2000:
            raise ValueError
        return value

    def to_url(self, value):
        #return '%04d' % value
        return str(value).zfill(4)

register_converter(YearConvertor, 'year')

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='homepage/index.html'), name='index'),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('articles/<year:year>/', views.article_year, name='articles_year'),
]
