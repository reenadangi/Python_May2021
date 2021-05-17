from django.shortcuts import render
from .forms import RegisterForm,UserRegisterForm

# Create your views here.
def index(request):
    myForm = RegisterForm()
    context = {"regForm": myForm}
    return render(request, 'index.html',context)
def register(request):
    pass
        