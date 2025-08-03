from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    context = {
        "current_year": datetime.date.today().year,
    }
      
    return render(request, 'index.html', context)
