from django.db import models

# Create your models here.
class travel_des(models.Model):
    name=models.CharField(max_length=300)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()

class travel_mate(models.Model):
    name=models.CharField(max_length=300)
    img=models.ImageField(upload_to='pics')
    description=models.TextField()