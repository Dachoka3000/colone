from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



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
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)