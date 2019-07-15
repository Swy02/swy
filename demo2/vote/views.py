from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login as lgi,logout as lgo,authenticate
from .forms import LoginForm
# Create your views here.
def checklogin(fun):
    def check(requst,*args):
        if requst.user and requst.user.is_authenticated:
            return fun(requst,*args)
        else:
            return redirect(reverse("vote:login"))
    return check

@checklogin
def index(request):
    desc=Question.objects.all()

    return render(request,'vote/index.html',locals())
@checklogin
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
@checklogin
def result(request,id):
    desc=Question.objects.get(pk=id)
    return render(request,'vote/result.html',locals())


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'vote/login.html',{'form':form})
    elif request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            lgi(request,user)
            return redirect(reverse("vote:index"))
        else:
            return render(request,'vote/login.html',{"errors":"登陆失败"})

        # form = LoginForm(request.POST)
        #
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        # user=authenticate(request,username=username,password=password)
        # if user:
        #     lgi(request,user)
        #     return redirect(reverse("vote:index"))
        # else:
        #     return render(request,'vote/login.html',{"errors":"登陆失败"})



def logout(request):
    lgo(request)
    return redirect(reverse('vote:login'))


def regist(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

    try:
        user=PullsUser.objects.create_user(username=username,password=password)

    except:
        user=None

    if user:
        return redirect(reverse("vote:login"))
    else:
        return render(request,'vote/html',{'errors':'注册失败'})