from django.shortcuts import render
import praw

# Create your views here.
reddit = praw.Reddit(client_id='aN2WWXxjRA3FPQ',
                     client_secret='bEN3500-jFK0oLSkMoU52ywCeTI',
                     user_agent='mac:prostalk:v0.0.1 (by nullbaka)')


def search_reddit(request):
    subreddit = reddit.subreddit('python')
    hot = subreddit.hot(limit=5)

    return render(request, 'explorer/reddit.html', {'hot': hot})


def comments(request, item):
    return render(request, 'explorer/comments.html', {'item': item})
