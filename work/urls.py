from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('project/',views.project, name = 'project'),
    path('projectdetail/<int:project_id>/', views.projectdetail, name = 'projectdetail'),
    path('uploadproject/',views.uploadproject, name='uploadproject'),
    path('searchproject/',views.filterproject, name='searchproject'),
    path('profile/',views.viewprofile, name='profile'),
    path('addprofile/',views.addprofile, name='addprofile'),
    path('addrating/<int:project_id>/', views.addrating, name='addrating'),
    path('calcrating/<int:project_id>/',views.calcratings, name='calcratings'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api-token-auth/',obtain_auth_token),
    re_path(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    re_path(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),

        
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)