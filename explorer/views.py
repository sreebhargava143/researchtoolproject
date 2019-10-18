from django.shortcuts import render
import praw
from .forms import SearchForm

reddit = praw.Reddit(client_id='aN2WWXxjRA3FPQ',
                     client_secret='bEN3500-jFK0oLSkMoU52ywCeTI',
                     user_agent='mac:prostalk:v0.0.1 (by nullbaka)')


# def search_reddit(request):
#     search_term = 'all'
#     if request.method=="POST":
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             search_term = form.cleaned_data.get('search_term')
#     subreddit = reddit.subreddit(search_term)
#     submissions = subreddit.top()
#     form = SearchForm()
#     return render(request, 'explorer/reddit.html', {'submissions': submissions, 'form': form})


# def search_subreddit(request):



# def comments(request, sub_name):
#     submission = reddit.info([sub_name])
#     for sub in submission:
#         author = sub.author
#         title = sub.title
#         text = sub.selftext
#         comments = sub.comments
#     return render(request, 'explorer/comments.html', {'comments': comments, 'text': text, 'title': title, 'author': author})
