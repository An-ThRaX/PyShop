from django.http import HttpResponse
from django.shortcuts import render
from .models import Product  # "." is the current folder
from .models import Offer
# /products -> index


def index(request):
    offers = Offer.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')


