from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'photos/', blank = True)
    description = models.TextField()
    link = models.URLField(max_length = 200)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True, blank =True)


class Profile(models.Model):
    pic = models.ImageField(upload_to='images/', blank = True)
    bio = models.TextField(blank=True)
    contact = models.TextField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)
