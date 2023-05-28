from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


Post = [

    {'title': 'The Lord',
     'content': 'The Lord is my shepherd, I shall not want',
     'date_posted': '27 May 2023'
     },

    {
        'title': 'A good day',
        'content': 'All things bright and beautiful, all creatures great and small, all things wise and wonderful, '
                   'the lord God made them all',
        'date_posted': '28 May 2923'
    }
]


def welcome(request):
    context = {
        'posts': Post
    }
    # return HttpResponse('Welcome to my blog app')
    return render(request, 'blog/welcome.html', context)


def about(request):
    contexts = {
        'posts': Post
    }
    return render(request, 'blog/welcome.html', contexts)


def say_hello(request):
    return HttpResponse("<h1>hi i'm james a ordinary boy learning how to be extra ordinary</h1>")
