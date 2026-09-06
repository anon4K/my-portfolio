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

def projects(request):
    software_projects = Project.objects.filter(category='software', is_published=True)
    hardware_projects = Project.objects.filter(category='hardware', is_published=True)
    return render(request, 'portfolio/projects.html', {
        'software_projects': software_projects,
        'hardware_projects': hardware_projects
    })
