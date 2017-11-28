from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    Task_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50, null=False)
    Description = models.CharField(max_length=500)
    Status = models.CharField(max_length=50, choices = [('Not Started','Not Started'),('In-Progress','In-Progress'),('Completed','Completed')])
    Author = models.CharField(max_length=50, null=False)
    Created_Date = models.DateTimeField(default=timezone.now, blank=True)
    Due_Date = models.DateTimeField(default=timezone.now, blank=True)
    User_name = models.ForeignKey('User', on_delete=models.CASCADE, related_name='usertask')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Task_id)

    def __str__(self):
        return str(self.User_name)

class Summary(models.Model):
    Title = models.CharField(max_length=50, null=False)
    Description = models.CharField(max_length=500)
    Status = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)

class User(models.Model):
    User_name = models.CharField(null=False, primary_key=True,max_length=50)
    First_name = models.CharField(max_length=50, null=False)
    Last_name = models.CharField(max_length=50, null=False)
    Email = models.CharField(max_length=50)

    def __str__(self):
        self.save()
        return str(self.User_name)


