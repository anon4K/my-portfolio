# portfolio/views.py
from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    projects = Project.objects.filter(is_published=True)
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about(request): 
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
