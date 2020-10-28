from django.shortcuts import render
from .models import Profile,Project

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
    except DoesNotExist:
        raise Http404()
    return render(request,'projectdetail.html', {"project": project})