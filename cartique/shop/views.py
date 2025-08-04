from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#index
def index(request):
    return render(request , 'shop/index.html')
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