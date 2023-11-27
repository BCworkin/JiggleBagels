from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

# not sure about this yet
def contact(request):
    return render(request, 'home/contact.html')