from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from DjangoUeditor.models import UEditorField

class Ads(models.Model):
    img=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=20)
    index=models.IntegerField(default=0)

class Category(models.Model):
    title=models.CharField(max_length=20)

class Tag(models.Model):
    title=models.CharField(max_length=20)

class Article(models.Model):
    title=models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    # body=models.TextField()
    body=UEditorField(imagePath='articleimg/',width="100%")
    tage=models.ManyToManyField(Tag)
