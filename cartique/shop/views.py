from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
#index
def index(request):
    products = list(Product.objects.all())
    slide_size = 3
    all_prods = [products[i:i + slide_size] for i in range(0, len(products), slide_size)]

    context = {
        'product_slides': all_prods,
        'slide_range': range(len(all_prods)),
    }
    return render(request, 'shop/index.html', context)


#about
def about(request):
    return render(request , 'shop/about.html')
#contact
def contact(request):
    return HttpResponse("This is the contact page. We are the service providers to custermers")
#tracking page 
def tracker(request):
    return HttpResponse("This is the tracker page. We are the service providers to you ,Check FAQ's here ")

def search(request):
    return HttpResponse("This is the search page. We are the service providers to custermers")

def productView(request):
    return HttpResponse("This is the productView page. We are the service providers to custermers")
 
def checkout(request):
    return HttpResponse("This is the checkout page. We are the service providers to custermers")