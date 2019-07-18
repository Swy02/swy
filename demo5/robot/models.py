from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField

class Ads(models.Model):
    img=models.ImageField(upload_to='ads')
    index=models.IntegerField(default=0)

class Course(models.Model):
    img=models.ImageField(upload_to='courseimg')
    title=models.CharField(max_length=20)
    title2=models.CharField(max_length=20)
    desc=models.CharField(max_length=50)

class Hon(models.Model):
    img=models.ImageField(upload_to='hon')

class School(models.Model):
    img=models.ImageField(upload_to='school')
    name=models.CharField(max_length=20)


class Teacher(models.Model):
    name=models.CharField(max_length=10)
    native=models.CharField(max_length=20)
    photos = models.ImageField(upload_to='teacher')

    def __str__(self):
        return self.name

class Titles(models.Model):
    title=models.CharField(max_length=30)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)


class Classes(models.Model):
    img=models.ImageField(upload_to='classesimg')

class News(models.Model):
    title=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    body=UEditorField()

    def __str__(self):
        return self.title


class Schoolnews(models.Model):
    title=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    views=models.IntegerField(default=0)
    body=UEditorField()

    def __str__(self):
        return self.title


class Register(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=5,choices=( ('man','男'),('woman','女')))
    age=models.CharField(max_length=10)
    number=models.IntegerField(max_length=11)

    def __str__(self):
        return self.name



