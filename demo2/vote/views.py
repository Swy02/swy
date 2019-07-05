from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    desc=Question.objects.all()

    return render(request,'vote/index.html',locals())

def detail(request,id):
    desc=Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'vote/detail.html',locals())
    elif request.method == "POST":
        choiced=request.POST.get('choice')
        choice=Choice.objects.get(pk=choiced)
        choice.num += 1
        choice.save()
        return redirect(reverse('vote:result',args=(id,)))

def result(request,id):
    desc=Question.objects.get(pk=id)
    return render(request,'vote/result.html',locals())