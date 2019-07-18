from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator,Page



class IndexView(View):
    def get(self, request):
        ads=Ads.objects.all()
        news=News.objects.all()
        schoolnews=Schoolnews.objects.all()

        return render(request,'robot/index.html',locals())

class About_us(View):
    def get(self,request):
        school=School.objects.all()
        hon=Hon.objects.all()
        pagenum = request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(hon,9).get_page(pagenum)
        return render(request,'robot/about_us.html',locals())

class NewsView(View):
    def get(self,request):
        news=News.objects.all()
        schoolnews=Schoolnews.objects.all()
        pagenum = request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(news, 5).get_page(pagenum)
        return render(request,'robot/news.html',locals())

class BaoMing(View):
    def get(self,request):
        return render(request,'robot/baoming.html',locals())

    def post(self,request):
        if request.POST.get("number") == "":
            return render(request,'robot/baoming.html')
        else:
            name = request.POST.get("name")
            gender = request.POST.get("sex")
            age = request.POST.get("age")
            number = request.POST.get("number")
            register = Register()
            register.name = name
            register.gender = gender
            register.age = age
            register.number = number
            register.save()
            return redirect(reverse("robot:baoming"))


class Competition(View):
    def get(self, request):
        hon=Hon.objects.all()
        pagenum = request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(hon,9).get_page(pagenum)
        return render(request, 'robot/competition.html',{'page':page,'hon':hon})


class Teachers_team(View):
    def get(self, request):
        teacher=Teacher.objects.all()
        pagenum = request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(teacher,2).get_page(pagenum)
        return render(request, 'robot/teachers_team.html',locals())


class Class_sys(View):
    def get(self, request):
        return render(request, 'robot/class_sys.html')


class Classroom_show(View):
    def get(self, request):
        classroom=Classes.objects.all()
        pagenum = request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(classroom, 9).get_page(pagenum)
        return render(request, 'robot/classroom_show.html',locals())


class Contact_us(View):
    def get(self, request):
        return render(request, 'robot/contact_us.html')



class Detail(View):
    def get(self, request,id):
        news=get_object_or_404(News,pk=id)
        news.views += 1
        news.save()
        return render(request, 'robot/news_details.html',locals())

class Detail1(View):
    def get(self, request, id):
        schoolnews = get_object_or_404(Schoolnews, pk=id)
        schoolnews.views += 1
        schoolnews.save()
        return render(request, 'robot/news_details1.html',locals())