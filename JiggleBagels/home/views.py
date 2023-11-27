from django.shortcuts import render
from items.models import Item, Category

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'home/index.html', {
        'categories': categories, 
        'items': items,
    })

# not sure about this yet
def contact(request):
    return render(request, 'home/contact.html')