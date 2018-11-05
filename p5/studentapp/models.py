from django.db import models

class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=50)
    dob=models.DateField()
    marks=models.FloatField()
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField()

