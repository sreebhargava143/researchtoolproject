from django.shortcuts import render

def explore(request):
    return render(request, 'explorer.html')