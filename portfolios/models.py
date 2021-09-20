from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('project/', null=True, blank=True)
    projectowner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = HTMLField(null=True, blank=True)
    livelink = models.URLField(null=True, blank=True)