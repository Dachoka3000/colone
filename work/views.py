from django.shortcuts import render,redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile,Project,Rating
from .forms import UploadProjectForm,AddProfileForm,AddRatingForm
from .filters import ProjectFilter


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

def viewprofile(request):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user)
    return render(request, 'profile.html',{"current_user":current_user, "profile":profile})

def addprofile(request):
    current_user = request.user

    if request.method == 'POST':
        form = AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = current_user
            new_profile.save()
            return redirect('profile')
    else:
        form=AddProfileForm()
    return render(request,'newprofile.html',{"form":form})

def filterproject(request):
    if request is None:
        return Project.objects.none()
    filter_list = Project.objects.all()
    project_filter = ProjectFilter(request.GET, queryset = filter_list)
    return render(request,'searchproject.html',{"filter":project_filter})

def addrating(request,project_id):
    project = Project.objects.get(id = project_id)
    current_user = request.user
    form = AddRatingForm()
    if request.method == 'POST':
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.project = project
            new_rating.human = current_user
            new_rating.save()

            return redirect('project')
        else:
            form = AddRatingForm()

    return render(request, 'rating.html',{'form':form,'project':project,'current_user':current_user})

def calcratings(request, project_id):
    primer = Project.objects.get(id=project_id)
    ratings = Rating.objects.filter(project=primer)
    sumdesign = 0
    sumusability = 0
    sumcontent = 0
    if len(ratings)>0:
        for rating in ratings:
            sumdesign +=rating.design
            meandesign = sumdesign/len(ratings)
            sumusability +=rating.usability
            meanusability = sumusability/ len(ratings)
            sumcontent +=rating.content
            meancontent = sumcontent/len(ratings)
            total = meandesign+ meanusability+ meancontent
            score = total/len(ratings)
        return score
    else:
        score = 0
        return score

