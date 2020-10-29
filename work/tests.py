from django.test import TestCase
from .models import Profile,Project
from django.contrib.auth import get_user_model

# Create your tests here.
class ProfileTestCase(TestCase):
    '''
    Test case class that runs test cases for profile obbjects
    '''

    def setUp(self):
        User = get_user_model()
        self.daisy = User.objects.create(username = "daisy", password = "mypassword")
        self.daisy.save()
        self.profile = Profile(pic = 'images/img.jpg',bio="love life",contact="daisy@email.com",user=self.daisy)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles))


