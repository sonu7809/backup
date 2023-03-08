from django.db import models

# Create your models here.
class Task(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    Description=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title