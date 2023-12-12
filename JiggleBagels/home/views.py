from django.shortcuts import render, redirect
from items.models import Item, Category
from .forms import SignUpForm

# Create your views here.
def index(request):
    
    username = None
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    # if the user is login, stored the user name
    if request.user.is_authenticated:
        # Access the username of the logged-in user
        username = request.user.username
    
    return render(request, 'home/index.html', {
        "username": username, 
        'categories': categories, 
        'items': items,
    })

def contact(request):
    return render(request, 'home/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html', {
        'form': form
    })
