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

    def designer(self):
        total = 0
        ratings = Rating.objects.filter(project=self)
        if len(ratings)>0:
            for rating in ratings:
                total += rating.design
                meandesignscore=total/len(ratings)
            return meandesignscore

        else:
            return 0

    def usable(self):
        total = 0
        ratings = Rating.objects.filter(project=self)
        if len(ratings)>0:
            for rating in ratings:
                total += rating.usability
                meanusabilityscore=total/len(ratings)
            return meanusabilityscore

        else:
            return 0

    def contenter(self):
        total = 0
        ratings = Rating.objects.filter(project=self)
        if len(ratings)>0:
            for rating in ratings:
                total += rating.content
                meancontentscore=total/len(ratings)
            return meancontentscore

        else:
            return 0

    def score(self):
        sumdesign = 0
        sumusability = 0
        sumcontent = 0
        ratings = Rating.objects.filter(project=self)
        if len(ratings)>0:
            for rating in ratings:
                sumdesign +=rating.design
                meandesign = sumdesign/len(ratings)
                sumusability +=rating.usability
                meanusability = sumusability/ len(ratings)
                sumcontent +=rating.content
                meancontent = sumcontent/len(ratings)
                total = meandesign+ meanusability+ meancontent
                
            return total/3
        else:
            return 0

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()



    def __str__(self):
        return self.title


class Profile(models.Model):
    pic = models.ImageField(upload_to='images/', blank = True)
    bio = models.TextField(blank=True)
    contact = models.TextField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

class Rating(models.Model):
    design = models.IntegerField(validators =[MinValueValidator(0),MaxValueValidator(10)] )
    usability = models.IntegerField(validators =[MinValueValidator(0),MaxValueValidator(10)] )
    content = models.IntegerField(validators =[MinValueValidator(0),MaxValueValidator(10)] )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    human = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()
    
