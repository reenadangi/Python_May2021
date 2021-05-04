from django.shortcuts import render, HttpResponse,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def directors(request):
    context={
        'directors':Director.objects.all()
    }
    return render(request,'directors.html',context)
    

def create_director(request):
    print(request.POST)
    
    director=Director.objects.create(
        name=request.POST['name']
    )
    
    return redirect('/directors')
   

def destroy_director(request,id):
    return HttpResponse(f"Delete director{id}")

def show_director(request,id):
    return HttpResponse(f"Show one director {id}")
    
def movies(request):
    context={
        'directors':Director.objects.all(),
        'movies':Movie.objects.all()
    }
    return render(request,'movies.html',context)

    

def create_movie(request):
    director=Director.objects.get(id=request.POST["director"])
    print(request.POST["director"])
    movie=Movie.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        director=director
    )
    return redirect('/movies')
    
def show_movie(request,id):
    return HttpResponse(f"Placeholder for show one movie {id}details")

def edit_movie(request,id):
    context={
        'movie':Movie.objects.get(id=id)
    }
    return render(request, 'edit_movie.html', context)
    

def update_movie(request,id):
    movie_to_update = Movie.objects.get(id=id)
    movie_to_update.title = request.POST['title']
    movie_to_update.description = request.POST['description']
    movie_to_update.save()
    return redirect('/movies')
    

def destroy_movie(request,id):
    movie_to_delete = Movie.objects.get(id=id)
    movie_to_delete.delete()
    return redirect('/movies')
    



