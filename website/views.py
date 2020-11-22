from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'masthead_title': 'Welcome to my very own web page!',
        'masthead_subtitle': "Please look around, I'm sure you'll find something interesting for you!"}
    return render(request, 'index.html', context)
