from django.shortcuts import render,redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile,Project
from .forms import UploadProjectForm


# Create your views here.
def home(request):

    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html',{"projects":projects})

def projectdetail(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'projectdetail.html', {"project": project})

def uploadproject(request):
    current_user= request.user 

    if request.method == 'POST':
        form = UploadProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = current_user
            new_project.save()
            return redirect('project')
    else:
        form=UploadProjectForm()
    return render(request,'newproject.html',{"form":form})

