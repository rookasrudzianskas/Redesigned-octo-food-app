from django.http import HttpResponse
from django.shortcuts import render
from .models import item
from  django.template import loader


# Create your viewss here.

def home(request):
    # item_list = item.Objects.all()
    template = loader.get_template('food/index.html')
    context = {
    }

    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse("Item!")
