from django.shortcuts import render
from .models import Services

def main_index(request):
    return render(request, 'main/index.html', {
        'posts': Services.objects.all()
    })

def main_about(request):
    return render(request, 'main/about.html')

def main_service(request):
    return render(request, 'main/services.html')

def main_contact(request):
    return render(request, 'main/contact.html')