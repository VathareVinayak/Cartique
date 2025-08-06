from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
#index
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4)
        # Group products in sublists of 4 items each
        prod_chunks = [prod[i:i + 4] for i in range(0, n, 4)]
        allProds.append([prod_chunks, range(1, nSlides + 1), nSlides, cat])
    
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


#about
def about(request):
    return render(request , 'shop/about.html')
#contact
def contact(request):
    return HttpResponse("This is the contact page. We are the service providers to custermers")
#tracking page 
def tracker(request):
    return HttpResponse("This is the tracker page. We are the service providers to you ,Check FAQ's here ")

# search page
def search(request):
    return HttpResponse("This is the search page. We are the service providers to custermers")

# product view
def productView(request):
    return HttpResponse("This is the productView page. We are the service providers to custermers")

# checkout page
def checkout(request):
    return HttpResponse("This is the checkout page. We are the service providers to custermers")