from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tweet 

# Create your views here.
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at',)

    return render(request, 'tweet_list.html', {'tweets': tweets})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id)
    
    return render(request, 'tweet_detail.html', {'tweet': tweet})
