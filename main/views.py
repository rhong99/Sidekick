from django.shortcuts import render


def home(request):
    title = 'Sidekick'
    context = {
        'title': title
    }
    return render(request, 'main/home.html', context)
