from django.shortcuts import render
from items.models import Item, Category
from .forms import SignUpForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'home/index.html', {
        'categories': categories, 
        'items': items,
    })

def contact(request):
    return render(request, 'home/contact.html')

def signup(request):
    form = SignUpForm()
    
    return render(request, 'home/signup.html', {
        'form': form,
    })
