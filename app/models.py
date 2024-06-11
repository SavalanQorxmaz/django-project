from typing import Any
from django.db import models
import base64
import re
from django.core.exceptions import ValidationError

# Create your models here.

class Contacts(models.Model):
  contact_title = models.CharField('Contact Title', max_length=100, unique=True)
  contact_link = models.CharField('Contact Link', max_length=500, unique=True)
  contact_logo = models.BinaryField(null=False, blank=False, editable=True )
  
class Logo(models.Model):
    logo_title = models.CharField('Logo Title', max_length=500, unique=True)
    logo = models.BinaryField(null=False, blank=False, editable=True)


class Slider(models.Model):
    slide = models.BinaryField(null=False, blank=False, editable=True)

class Projects(models.Model):
    name = models.CharField('Project Name', max_length=100, unique=True, blank=False,)
    Description = models.TextField('Tag Description', max_length=1000, blank=True)
    # class Meta:
    #    ordering = ('name',)
    def __str__(self):
        return self.name
    def clean(self):
        regex = re.findall("[\\,/,!,#,@,$,%,^,&,*,(,),]", self.name)
        if not len(regex) <1:
            raise ValidationError(
                {'name': "Not !@#$%^&*()"})



class Photos(models.Model):
    photo_name = models.CharField('Photo Name', max_length=200, unique=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, default=None)
    photo = models.BinaryField(null=False, blank=False, editable=True)


class Project(models.Model):
    title =models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField(null=True, blank=True)
    class Meta:
       ordering = ('title',)
    def __str__(self):
        return self.title

class Picture(models.Model):
    content_type = models.ForeignKey(Project, on_delete=models.CASCADE)
    imgtitle =models.CharField(max_length=20)
    image = models.BinaryField(null=True, blank=True, editable=True )