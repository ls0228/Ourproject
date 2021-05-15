from django.shortcuts import render

def news_(request):
    return render(request, 'news/news.html')
