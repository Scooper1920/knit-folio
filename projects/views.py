from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm

def list_projects(request):
    projects=Project.objects.all()

    return render(request, "projects/list_projects.html",
                    {"projects":projects})

def project_detail(request,pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project':project
    }
    return render(request, 'projects/project_detail.html',context)

def add_project(request):
    if request.method == 'GET':
        form = ProjectForm()
    else:
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_projects')
            
    return render(request, "projects/add_project.html", {"form":form})


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'GET':
        form = ProjectForm(instance=project)
    else:
        form = ProjectForm(data=request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect(to='list_projects')

    return render(request, "projects/edit_project.html", {
        "form": form,
        "project": project
    })


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect(to='list_projects')

    return render(request, "projects/delete_project.html",
                  {"project": project})



# Create your views here.
