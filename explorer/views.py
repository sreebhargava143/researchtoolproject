from django.shortcuts import render
import praw
from .forms import SearchForm

reddit = praw.Reddit(client_id='aN2WWXxjRA3FPQ',
                     client_secret='bEN3500-jFK0oLSkMoU52ywCeTI',
                     user_agent='mac:prostalk:v0.0.1 (by nullbaka)')


def search_reddit(request):
    all = reddit.subreddit('all')
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('search_term')
            result = all.search(query, limit=250)
    else:
        result = all.top()
        
    form = SearchForm()
    return render(request, 'explorer/reddit.html', {'result':result, 'form': form})


# def search_subreddit(request):



def comments(request, sub_name):
    submission = reddit.info([sub_name])
    for sub in submission:
        author = sub.author
        title = sub.title
        text = sub.selftext
        comments = sub.comments
    return render(request, 'explorer/comments.html', {'comments': comments, 'text': text, 'title': title, 'author': author})


def explore(request):
    all = reddit.subreddit('all')
    result = all.top()
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('search_term')
            result = all.search(query, limit=250)
        
    form = SearchForm
    return render(request, 'explorer.html', {'result': result, 'form': form})
