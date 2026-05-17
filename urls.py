from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('author/<str:author_name>/', views.articles_by_author, name='articles_by_author'),
]
