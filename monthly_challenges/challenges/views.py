from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def january(request):
    return HttpResponse("eat no meat")


def feb(request):
    return HttpResponse("walk for at least 20 minutes per day")


def march(request):
    return HttpResponse("Learn django at least 20 munites per day")


def monthly_challenge(request, month):
    challange_text = None
    if month == 'january':
        challange_text = "eat no meat"
    elif month == 'february':
        challange_text = "walk for at least 20 minutes per day"
    elif month == 'march':
        challange_text = "<h1>Learn django at least 20 munites per day<h1>"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challange_text)
