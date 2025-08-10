from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Contact
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
    if(request.method == "POST"):
        # Handle the contact form submission
        name = request.POST.get('name','')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # saving the messages contact details send an email
        print(f"Name: {name}, Email: {email}, Message: {message}")
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return HttpResponse("Thank you for contacting us!")
    return render(request , 'shop/contact.html')
#tracking page 
def tracker(request):
    return render(request , 'shop/tracker.html')

# search page
def search(request):
    return render(request , 'shop/search.html')

# product view
def productView(request , myid):
    # fetch product details
    product = Product.objects.get(id=myid)
    print(product)
    return render(request , 'shop/productview.html', {'product': product})

# checkout page
def checkout(request):
    return render(request , 'shop/checkout.html')