from django.shortcuts import render, redirect
from .models import Genre, Movie
import base64
from .forms import SearchForm
from django.db import models
from django.core import serializers
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    if request.method == "POST":
        selected_genres = request.POST.getlist("genres")
        movies = Movie.objects.filter(genres__in=selected_genres).distinct()
        movies_data = serializers.serialize("json", movies)
        request.session["movies"] = movies_data
        return redirect("page2")
    else:
        genres = Genre.objects.all()
        movies = Movie.objects.all()
        for movie in movies:
            if movie.thumbnail:
                movie.thumbnail = base64.b64encode(movie.thumbnail).decode('utf-8')
        items_per_page = 10
        paginator = Paginator(movies, items_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context = {"genres": genres, 'movies': page}
        return render(request, "index.html", context)

def search(request):
    return render(request, 'search.html')

def search_movies(request):
    form = SearchForm(request.GET)
    movies = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        print(query)
        if query:
            movies = Movie.objects.filter(
                models.Q(name__icontains=query) |
                models.Q(year__icontains=query) |
                models.Q(director__icontains=query) |
                models.Q(country__icontains=query) 
            )
    print(movies)
    context = {'form': form, 'movies': movies}
    return render(request, 'search_movies.html', context)

def page2(request):
    try:
        movies_data = request.session["movies"]
        if movies_data:
            movies = serializers.deserialize('json', movies_data)
            movies = [movie.object for movie in movies]
        else:
            movies = []
        if movies:
            i = 0
            for movie in movies:
                if movie.thumbnail:
                    movie.thumbnail = base64.b64encode(movie.thumbnail).decode('utf-8')
                if i == 0:
                    movie.active = True
                movie.data_slide_to = i
                i += 1
            context = {
                "movies": movies
            }
            return render(request, "page2.html", context)
        else:
            return render(request, "notfoundpage.html")
    except KeyError:
        return redirect("index")
