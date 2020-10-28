from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'photos/', blank = True)
    description = models.TextField()
    link = models.URLField(max_length = 200)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True, null =True)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(project=self)
        return len(ratings)

    def __str__(self):
        return self.title


class Profile(models.Model):
    pic = models.ImageField(upload_to='images/', blank = True)
    bio = models.TextField(blank=True)
    contact = models.TextField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class Rating(models.Model):
    design = models.IntegerField(validators =[MinValueValidator(0),MaxValueValidator(10)] )
    usability = models.IntegerField(validators =[MinValueValidator(0),MaxValueValidator(10)] )
    content = models.IntegerField(validators =[MinValueValidator(0),MaxValueValidator(10)] )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    human = models.ForeignKey(User, on_delete=models.CASCADE)
    
