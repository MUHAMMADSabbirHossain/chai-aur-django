from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Tweet 
from .forms import TweetForm

# Create your views here.
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at',)

    return render(request, 'tweet_list.html', {'tweets': tweets})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id)
    
    return render(request, 'tweet_detail.html', {'tweet': tweet})

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        valid = form.is_valid()

        if valid:
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()

            return redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweet_create.html', {'form': form})

def tweet_update(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance = tweet)
        valid = form.is_valid()

        if valid:
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()

            return redirect('tweet_list')
    else:
        form = TweetForm(instance = tweet)

    return render(request, 'tweet_update.html', {'form': form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)

    if request.method == "POST":
        tweet.delete()

        return redirect('tweet_list')
    
    return render(request, 'tweet_delete.html', {'tweet': tweet})
