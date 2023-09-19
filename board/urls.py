from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write_article, name='write_article'),
]
