from django.shortcuts import render

def index_view(requests):
    return render(requests, 'index.html', {'heading':'Recipe Box.'})
