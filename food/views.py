from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse("Rokas!")


def item(request):
    return HttpResponse("Item!")
