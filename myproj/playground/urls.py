from django.urls import path
from . import views


app_name = 'playground'

urlpatterns = [
    path('', views.IndexView.as_view()),
]