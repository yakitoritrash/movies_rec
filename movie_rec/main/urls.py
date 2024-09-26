from django.urls import path
from .views import index, page2, search, search_movies

urlpatterns = [
    path("", index, name="index"),
    path('search/', search, name='search'),
    path('search/result/', search_movies, name='search_movies'),
    path("page2/", page2, name="page2"),
]
