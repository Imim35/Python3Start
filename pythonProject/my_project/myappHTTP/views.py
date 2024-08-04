import datetime
from django.shortcuts import render


# Create your views here.

def index(request):
    today = datetime.datetime.now().date()
    # other view code here
    return render(request, 'index.html', {"today": today})
