from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World! You are at chai aur Django Home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, World! You are at chai aur Django About page.")

def contact(request):
    return HttpResponse("Hello, World! You are at chai aur Django Contact page.")