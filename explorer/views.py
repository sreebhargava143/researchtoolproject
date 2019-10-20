from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import praw #reddit api module


@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'explorer.html')

@login_required(login_url='/accounts/login/')
def explorer_hot_feeds(request):
    # reddit = praw.Reddit(
    #     client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    # subreddit = reddit.subreddit('all')
    # feeds = subreddit.hot(limit=10)
    context = {
        'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_top_feeds(request):
    # reddit = praw.Reddit(
    #     client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    # subreddit = reddit.subreddit('all')
    # feeds = subreddit.top(limit=10)
    context = {
        # 'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_rising_feeds(request):
    # reddit = praw.Reddit(
    #     client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    # subreddit = reddit.subreddit('all')
    # feeds = subreddit.rising(limit=10)
    context = {
        # 'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_controversial_feeds(request):
    # reddit = praw.Reddit(
    #     client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    # subreddit = reddit.subreddit('all')
    # feeds = subreddit.controversial(limit=10)
    context = {
        # 'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_new_feeds(request):
    # reddit = praw.Reddit(
    #     client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    # subreddit = reddit.subreddit('all')
    # feeds = subreddit.new(limit=10)
    context = {
        # 'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

