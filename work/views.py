from django.shortcuts import render,redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Rating
from .forms import UploadProjectForm,AddProfileForm,AddRatingForm
from .filters import ProjectFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import ProfileSerializer,ProjectSerializer
from .permissions import IsAdminOrReadOnly,IsAuthenticatedOrReadOnly


# Create your views here.
def home(request):
    project=Project.objects.first()

    return render(request,'home.html', {"project":project})

def about(request):
    return render(request, 'about.html')

@login_required(login_url='/accounts/login/') 
def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html',{"projects":projects})

@login_required(login_url='/accounts/login/') 
def projectdetail(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'projectdetail.html', {"project": project})

@login_required(login_url='/accounts/login/') 
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

@login_required(login_url='/accounts/login/') 
def viewprofile(request):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user)
    projects = Project.objects.filter(owner = current_user)
    return render(request, 'profile.html',{"current_user":current_user, "profile":profile, "projects":projects})

@login_required(login_url='/accounts/login/') 
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

@login_required(login_url='/accounts/login/') 
def filterproject(request):
    if request is None:
        return Project.objects.none()
    filter_list = Project.objects.all()
    project_filter = ProjectFilter(request.GET, queryset = filter_list)
    return render(request,'searchproject.html',{"filter":project_filter})


@login_required(login_url='/accounts/login/') 
def addrating(request,project_id):
    project = Project.objects.get(id = project_id)
    current_user = request.user
    form = AddRatingForm()
    if request.method == 'POST':
        form = AddRatingForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data.get("design")
            usability = form.cleaned_data.get("usability")
            content = form.cleaned_data.get("content")
            new_rating = Rating(design=design, usability=usability, content=content, human=current_user, project=project)
            new_rating.save()
            return redirect('project')
        else:
            form = AddRatingForm()

    return render(request, 'rating.html',{'form':form,'project':project,'current_user':current_user})

@login_required(login_url='/accounts/login/') 
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
        return {"score":score, "meandesign":meandesign,"meanusability":meanusability,"meancontent":meancontent,"primer":primer,"ratings":ratings}
    else:
        score = 0
        messa
        return score
    return render(request,'score.html')


class ProjectList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers=ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers=ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDescription(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly)
    def get_project(self,pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)


class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self,pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_profile(pk)
        serializers = ProfileSerializer(project)
        return Response(serializers.data)


    


