from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('project/', null=True, blank=True)
    projectowner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = HTMLField(null=True, blank=True)
    livelink = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def delete_project(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_description(cls, id, description):
        cls.objects.filter(id=id).update(description=description)