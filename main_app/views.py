from django.shortcuts import render
from main_app.models import Product

# Create your views here.
def main(request):
    return render(request, 'main.html')

def catalog(request):
    item = Product.objects.all()
    return render(request, 'catalog.html', {'item':item})

def contacts(request):
    return render(request, 'contacts.html')

def long1(request):
    item = Product.objects.all()
    return render(request, 'long1.html', {'item':item})

def long2(request):
    item = Product.objects.all()
    return render(request, 'long2.html', {'item':item})

def long3(request):
    item = Product.objects.all()
    return render(request, 'long3.html', {'item':item})

def long4(request):
    item = Product.objects.all()
    return render(request, 'long4.html', {'item':item})
