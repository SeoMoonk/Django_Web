from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write_article, name='write_article'),
    path('add/', views.add, name='add_article'),
    path('<int:article_id>/', views.view, name='view_article'),
]

