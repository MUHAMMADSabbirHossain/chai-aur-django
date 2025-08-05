from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet 

# Create your views here.
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')

    return render(request, 'tweet_list.html', {'tweets': tweets})
