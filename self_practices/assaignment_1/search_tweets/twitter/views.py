from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tweet_list(request):
    return render(request, 'tweet_list.html')
