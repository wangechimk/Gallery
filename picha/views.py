from django.shortcuts import render
from .models import Images


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def gallery(request):
    pictures = Images.get_all()
    return render(request, 'gallery.html', {'pictures': pictures})