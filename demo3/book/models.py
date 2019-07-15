from django.db import models
# Create your models here.

class BookInfo(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20,choices=(('man','男'),('woman','女')))
    content=models.CharField(max_length=20)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name






