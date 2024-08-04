from django.shortcuts import render


# Create your views here.

def index(request):
    # other view code here
    return render(request, 'products.html', {})
