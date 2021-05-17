from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact page</h1>")


def about_view(request, *args, **kwargs):
    my_context = {
        "name": "hello",
        "number": 12,
        "lists": [12, 34, 56, 78, 90]
    }
    return render(request, "about.html", my_context)
