from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import praw #reddit api module


@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'explorer.html')

@login_required(login_url='/accounts/login/')
def explorer_hot_feeds(request):
    context = {
        'page':"search",
        'query':'hot-news',
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_top_feeds(request):
    context = {
        "page":"search",
        "query":"top-news"
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_rising_feeds(request):
    context = {
        "page":"search",
        "query":"rising"
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_controversial_feeds(request):
    context = {
        "page":"search",
        "query":"controversy"
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_new_feeds(request):
    context = {
        "page":"search",
        "query":"latest-news"
    }
    return render(request, 'explorer.html', context=context)

@login_required(login_url='/accounts/login/')
def explorer_search(request):
    print(request.GET.get("query"))
    context = {
        "page":"search",
        "query":request.GET.get("query")
    }
    return render(request, 'explorer.html', context=context)

def explorer_bookmarks(request):
    context = {
        "page": "bookmarks"
    }
    return render(request, 'explorer_bookmarks.html', context=context)