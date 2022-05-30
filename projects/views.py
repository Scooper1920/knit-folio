from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm,CreateUserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register_page(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
#above line is if the method is post then put data into the form
#then validate form
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
#above line of code will get only the argument from the form
            messages.success(request, "Yass! Profile Created for " + user )
            return redirect('login_page')
#once user is registered they can login
    context ={'form':form}
    return render(request, 'projects/register_page.html',context)


def login_page(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)
#the word login and logout is a django method 
            return redirect('list_projects')
        else:
            messages.info(request,"Try again, buster! Wrong username or password!")
            
        
    context={}
    return render(request,'projects/login_page.html', context )


def log_out(request):
    logout(request)
    return redirect ('login_page')
#no template needed here

    
@login_required(login_url="login_page")
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





def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect(to='list_projects')

    return render(request, "projects/delete_project.html",
                  {"project": project})



# Create your views here.
