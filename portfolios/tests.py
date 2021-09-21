
from django.test import TestCase
from .models import Projects, Profile
from django.contrib.auth.models import User

class TestProjects(TestCase):
  def setUp(self):
    self.newproject = Projects(title='Delani Studion', image='test.jpg', projectowner= User.objects.create(username='JosephKinyua'), description='a clone for delani studio', livelink='http://google.com/?search=this+is+amazing')
    self.newproject.save_project()

  def teardown(self):
    User.objects.all().delete()
    Projects.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.newproject, Projects))

  def test_saveProject(self):
    self.assertEqual(len(Projects.objects.all()),1) 

  def test_deleteProject(self):
    self.new_project2 = Projects(title='4life', image='test.jpg', projectowner=User.objects.create(username='Kinyuajoseph2014'), description='a Webapp fro gbv victims', livelink='http://gbv.com/about')
    self.new_project2.save_project()
    self.assertEqual(len(Projects.objects.all()),2)
    Projects.delete_project(self.new_project2.id)
    self.assertEqual(len(Projects.objects.all()),1)

  def test_updateProject(self):
    Projects.update_description(self.newproject.id, 'this is amazing')
    updated_post = Projects.objects.get(id=self.newproject.id)
    self.assertEqual(updated_post.description,  'this is amazing')

  def test_allprojects(self):
    self.new_project2 = Projects(title='4life', image='test.jpg', projectowner=User.objects.create(username='maingi'), description='a Webapp fro gbv victims', livelink='http://gbv.com/about')
    self.new_project2.save_project()
    self.assertEqual(len(Projects.all_projects()), 2)

  def test_userprojects(self):
    self.new_project2 = Projects(title='4life', image='test.jpg', projectowner=User.objects.create(username='maingi'), description='a Webapp fro gbv victims', livelink='http://gbv.com/about')
    self.new_project2.save_project()
    usrpic = Projects.user_projects(self.new_project2.projectowner.username)
    self.assertEqual(len(usrpic), 1)

class TestProfile(TestCase):
  def setUp(self):
    self.new_user = User(username = "JosephKinyua")
    self.new_user.save()
    self.newprofile = Profile.objects.create(profilePic='test.jpg', bio='i am amazing')

  def tearDown(self):
    Profile.objects.all().delete()
    User.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.newprofile, Profile))
