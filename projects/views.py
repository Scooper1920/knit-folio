from django.shortcuts import render, redirect, get_object_or_404
from .models import Project

def list_projects(request):
    projects=Project.objects.all()

    return render(request, "projects/list_projects.html",
                    {"projects":projects})




# Create your views here.
