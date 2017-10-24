from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def catalog(request):
    return render(request, 'catalog.html')

def contacts(request):
    return render(request, 'contacts.html')

def long1(request):
    return render(request, 'long1.html')

def long2(request):
    return render(request, 'long2.html')

def long3(request):
    return render(request, 'long3.html')

def long4(request):
    return render(request, 'long4.html')