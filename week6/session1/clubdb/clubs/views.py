from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    # check if user is in session - redirect to clubs
    return render(request,"index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
        # Validate form data 
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        # Register User
        new_user = User.objects.register(request.POST)
        # Put user in session
        request.session['user_id'] = new_user.id
        # Redirect to main page clubs 
        return redirect("/clubs")
    return redirect("/clubs")

def login(request):
    if request.method == "GET":
        return redirect('/')
    # Authenticate 
    # Get user
    # Put user in session
    return redirect("/clubs")

def logout(request):
    # clear session
    return redirect('/')

def clubs(request):
    # Make sure user us logged in
    context = {
		"user": "user",
        "user_clubs": "user_clubs",
        "member" : "members",
        "other_clubs": "other_clubs",
    
	}
    return render(request,"clubs.html",context)

def new(request):
    if 'user_id' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return render(request,"addclub.html",context)

def create(request):
    if request.method == "POST":
        errors = Club.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/clubs/new")
        Club.objects.create(
            name =request.POST['name'],
            desc=request.POST['desc'],
            date_start = request.POST['date_start'],
		    date_end = request.POST['date_end'],
            owner=User.objects.get(id=request.session['user_id'])
        )
    return redirect("/clubs")

def edit(request,id):
    pass

def update(request,id):
    pass

def show(request, c_id):
    pass

def join(request,c_id):
    pass

def drop(request,c_id):
    pass

def delete(request,id):
    pass
