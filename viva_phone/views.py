from django.shortcuts import render
from .models import feature_item
# Create your views here.
def Home(request):    
	return render(request, 'index.html', {})

def Features(request):
    items = list(feature_item.objects.all())
    return render(request, 'features.html', {'items':items})

def Download(request):    
	return render(request, 'download.html', {})