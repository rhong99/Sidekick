from django.shortcuts import render
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'User/home.html', context)
