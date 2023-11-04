from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import ProjectForm
# from .models import Project

def site_home(request):
    context = {
        'context': 'context',

    }
    return render(request, 'school_website/home.html', context)