from django.db import models

class Task(models.Model):
    title =models.CharField(max_length=50)
    description =models.CharField(max_length=500)
    due_date =models.DateTimeField()
    priority =models.CharField(max_length=20)
    completed =models.BooleanField()
   
    
