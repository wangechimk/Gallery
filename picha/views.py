from django.shortcuts import render
from .models import Images


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def gallery(request):
    pictures = Images.get_all()
    return render(request, 'gallery.html', {'pictures': pictures})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        res = Images.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'results':res})
    else:
        message = 'You have not searched any term'
        return render(request, 'search.html', {'message':message}) 
