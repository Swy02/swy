from django.shortcuts import render,redirect,reverse
from .models import *
# Create your views here.

def index(request):
    username='swy'
    return render(request,'book/index.html',locals(),)


def list(request):
    book=BookInfo.objects.all()
    return render(request,'book/list.html',locals())


def detail(request,id):
    book=BookInfo.objects.get(pk=id)
    return render(request,'book/detail.html',locals())

def addHero(request,id):
    book=BookInfo.objects.get(pk=id)
    if request.method == "GET":
        return render(request,'book/addhero.html',locals())
    elif request.method == "POST":
        name=request.POST.get("username")
        content=request.POST.get('content')
        gender=request.POST.get('gender')
        hero=HeroInfo()
        hero.name=name
        hero.content=content
        hero.gender=gender
        hero.book=book
        hero.save()
        return redirect(reverse('book:detail',args=(id,)))


def deleteHero(request,id):
    hero=HeroInfo.objects.get(pk=id)
    hero.delete()
    bookid = hero.book.id
    return redirect(reverse("book:detail",args=(bookid,)))