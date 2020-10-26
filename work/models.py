from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_t0 = 'photos/', blank = True)
    description = models.TextField()
    link = models.URLField(max_length = 200)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True, blank =True)
