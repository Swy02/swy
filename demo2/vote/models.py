from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    desc=models.CharField(max_length=30)
    create_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc


class Choice(models.Model):
    desc=models.CharField(max_length=20)
    num=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.desc


class PullsUser(User):
    telepone=models.CharField(max_length=11)

