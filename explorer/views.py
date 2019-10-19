from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import praw

@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'explorer.html')

@login_required(login_url='/accounts/login/')
def explorer_hot_feeds(request):
    reddit = praw.Reddit(
        client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    subreddit = reddit.subreddit('all')
    feeds = subreddit.hot(limit=10)
    context = {
        'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_top_feeds(request):
    reddit = praw.Reddit(
        client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    subreddit = reddit.subreddit('all')
    feeds = subreddit.top(limit=10)
    context = {
        'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_rising_feeds(request):
    reddit = praw.Reddit(
        client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    subreddit = reddit.subreddit('all')
    feeds = subreddit.rising(limit=10)
    context = {
        'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_controversial_feeds(request):
    reddit = praw.Reddit(
        client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    subreddit = reddit.subreddit('all')
    feeds = subreddit.controversial(limit=10)
    context = {
        'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_new_feeds(request):
    reddit = praw.Reddit(
        client_id='xWAHngnw1APo7w',client_secret='Ffpx4FrMk2Q1cSzOAAZTDhjRK_A',user_agent="storead")
    subreddit = reddit.subreddit('all')
    feeds = subreddit.new(limit=10)
    context = {
        'feeds':feeds,
    }
    return render(request, 'explorer.html', context=context)


# uttaran


# <<<<<<< praw
# import praw
# from .forms import SearchForm
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.forms.models import model_to_dict

# reddit = praw.Reddit(client_id='aN2WWXxjRA3FPQ',
#                      client_secret='bEN3500-jFK0oLSkMoU52ywCeTI',
#                      user_agent='mac:prostalk:v0.0.1 (by nullbaka)')


# def search_reddit(request):
#     all = reddit.subreddit('all')
#     if request.method=="POST":
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             query = form.cleaned_data.get('search_term')
#             result = all.search(query, limit=250)
#     else:
#         result = all.top()
        
#     form = SearchForm()
#     return render(request, 'explorer/reddit.html', {'result':result, 'form': form})


# def search_subreddit(request):



# def comments(request, sub_name):
#     submission = reddit.info([sub_name])
#     for sub in submission:
#         author = sub.author
#         title = sub.title
#         text = sub.selftext
#         comments = sub.comments
#     return render(request, 'explorer/comments.html', {'comments': comments, 'text': text, 'title': title, 'author': author})

# =======
# <<<<<<< praw
#     all = reddit.subreddit('all')
#     result = all.top()
#     if request.method == "GET":
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data.get('search_term')
#             result = all.search(query, limit=250)
        
#     form = SearchForm
#     return render(request, 'explorer.html', {'result': result, 'form': form})



# def submissions_json_list(subreddit):
#     submissions = []
#     for submission in subreddit.top(limit=3):
#         dic = {
#             "name": submission.name,
#             "title": submission.title,
#             "author": submission.author,
#             "selftext": submission.selftext,
#             "created_utc": submission.created_utc,
#             "subreddit": submission.subreddit.display_name,
#             "subreddit_name":submission.subreddit.name,
#             "url": submission.url,
#             "score": submission.score
#         }
#         submissions.append(dic)
#         dic = {}
#     return submissions



# def subreddit_to_json(request, subreddit_name):
#     subreddit = reddit.subreddit(subreddit_name)
#     subreddit_json = {
#         "name": subreddit.name,
#         "display_name": subreddit.display_name,
#         "public_description": subreddit.public_description,
#         "created_utc": subreddit.created_utc,
#         "subcsribers": subreddit.subscribers,
#         "submissions": submissions_json_list(subreddit)
#     }
#     return JsonResponse(subreddit_json)


# def comments_json_list(submission):
#     comments = []
#     for comment in submission.comments:
#         dic = {
#             "body": comment.body,
#             "created_utc": comment.created_utc,
#             "id": comment.id,
#             "parent_id": comment.parent_id
#         }
#         comments.append(dic)
#         dic = {}
#     return comments


# def submission_to_json(request, id):
#     submission = reddit.submission(id)
#     submission_json = {
#         "title": submission.title,
#         "author": submission.author.name,
#         "id": submission.id,
#         "created_utc": submission.created_utc,
#         "selftext": submission.selftext,
#         "score": submission.score,
#         "subreddit": submission.subreddit.display_name,
#         "url": submission.url,
#         "comments": comments_json_list(submission)
#     }
#     return JsonResponse(submission_json)
# =======






