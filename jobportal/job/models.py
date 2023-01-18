from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Students(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phoneNo=models.CharField(max_length=15,null=True)
    #image=models.FileField(null=True)
    #gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=10,null=True)
    def _str_(self):
        return self.user.username

class Company(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=100,null=True)
    phoneNo=models.CharField(max_length=15,null=True)
    #image=models.FileField(null=True)
    #gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=20,null=True)
    def _str_(self):
        return self.user.username

class Jobs(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    startDate=models.DateField()
    endDate=models.DateField()
    title=models.CharField(max_length=100)
    #image=models.FileField(null=True)
    #gender=models.CharField(max_length=10,null=True)
    salary=models.FloatField(max_length=20)
    description=models.CharField(max_length=300)
    experience=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)
    creationDate=models.DateField()
    def _str_(self):
        return self.title

class applyJob(models.Model):
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    student=models.ForeignKey(Students,on_delete=models.CASCADE)
    resume=models.FileField(null=True)
    applyDate=models.DateField()
    def _str_(self):
        return self.id