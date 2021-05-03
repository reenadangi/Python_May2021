from django.shortcuts import render, HttpResponse,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def directors(request):
    return HttpResponse(f"Placeholder for all directors")
    

def create_director(request):
    return HttpResponse(f"Add a new director in DB")
   

def destroy_director(request,id):
    return HttpResponse(f"Delete director{id}")

def show_director(request,id):
    return HttpResponse(f"Show one director {id}")
    
def movies(request):
    return HttpResponse(f"Placeholder for all Movies")

def create_movie(request):
    return HttpResponse(f"Add a new Movie in DB")
    
def show_movie(request,id):
    return HttpResponse(f"Placeholder for show one movie {id}details")

def edit_movie(request,id):
    return HttpResponse(f"Placeholder for Edit movie {id}")
    

def update_movie(request,id):
    return HttpResponse(f"Placeholder for updating movie {id} in database")
    

def destroy_movie(request,id):
    return HttpResponse(f"Placeholder for deleting movie{id}")
    



