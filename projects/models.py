from django.db import models

class Project(models.Model):
    image=models.ImageField(upload_to='img/'),
    title=models.CharField(max_length=100),
    patternlnk=models.URLField(blank=True,null=True),
    yarn = models.CharField(max_length=100),
    meters = models.IntegerField(null=True, blank=True),
    dateStart= models.DateField(null=True, blank =True),
    dateDone = models.DateField(null=True, blank=True),
    description = models.TextField(null=True, blank=True),
