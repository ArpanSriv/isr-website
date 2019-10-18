from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def ngos(request):
    return render(request, 'ngos.html')

def forms(request):
    return render(request, 'forms.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')