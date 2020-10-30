from django.test import TestCase
from .models import Profile,Project,Rating
from django.contrib.auth import get_user_model

# Create your tests here.
class ProfileTestCase(TestCase):
    '''
    Test case class that runs test cases for profile obbjects
    '''

    def setUp(self):
        User = get_user_model()
        self.daisy = User(username = "daisy", email="daisy@email.com", password = "mypassword")
        self.daisy.save()
        self.profile = Profile(bio="love life",contact="daisy@email.com",user=self.daisy)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_update_method(self):
        self.profile.save_profile()
        self.profile = Profile.objects.filter(contact = 'daisy@email.com').update(contact = 'maisy@email.com')
        self.profile_update = Profile.objects.get(bio="love life")
        self.assertTrue(self.profile_update.contact== 'maisy@email.com')

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile=Profile.objects.get(bio='love life')
        self.profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)

class ProjectTestCase(TestCase):
    '''
    TestCase that runs test cases for project objects
    '''

    def setUp(self):
        User = get_user_model()
        self.machoka = User(username = "machoka",email="machoka@email.com",password="password")
        self.machoka.save()
        self.project = Project(title="Instaclone", description="Instagram clone", link="http://insta.heroku.com",owner=self.machoka)

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.project.save_project()
        self.project=Project.objects.get(title="Instaclone")
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

class RatingTestCase(TestCase):
    '''
    Test case that runs test cases for rating objects
    '''

    def setUp(self):
        User = get_user_model()
        self.mary = User(username = "mary",email="mary@email.com",password="password")
        self.mary.save()
        self.sample = Project(title="Akan", description="akan names", link="http://akan.heroku.com",owner=self.mary)
        self.sample.save()
        self.rating=Rating(design=1,usability=4,content=6,project=self.sample,human=self.mary)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating,Rating))

    def test_save_method(self):
        self.rating.save_rating()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)>0)

    def test_delete_method(self):
        self.rating.save_rating()
        self.rating=Rating.objects.get(human=self.mary)
        self.rating.delete_rating()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)==0)

        

        





