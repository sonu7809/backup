from django.db import models

# Create your models here.
#company
class company(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    about=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=(('IT','IT'),('nonit','nonit'),('mobile','mobile')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
