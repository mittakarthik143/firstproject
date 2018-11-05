from django.db import models

class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eadd=models.TextField()

    def __str__(self):
        return self.ename
