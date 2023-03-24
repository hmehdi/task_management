from django.db import models

class Task(models.Model):
    title =models.CharField(max_length=50)
    desc =models.CharField(max_length=500)
   
    
