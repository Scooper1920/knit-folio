from django.db import models

class Project(models.Model):
    image=models.ImageField(upload_to='img/', null=True)
    title=models.CharField(max_length=100, null=True)
    patternlnk=models.URLField(blank=True,null=True)
    yarn = models.CharField(max_length=100, null=True)
    meters = models.IntegerField(null=True, blank=True)
    dateStart= models.DateField(null=True, blank =True)
    dateDone = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
