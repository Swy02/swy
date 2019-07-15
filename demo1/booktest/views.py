from django.shortcuts import render ,reverse ,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.template import loader
from .models import BookInfo,HeroInfo


def index(request):
    # return HttpResponse('这是首页' "<a href='/booktest/list/'>跳转列表页</a>")
    # 1.获取模板
    temp1=loader.get_template('booktest/index.html')
    # 2.使用模板渲染字典参数
    result=temp1.render({'username':'swy'})
    # 3.将渲染的结果返回
    return HttpResponse(result)

def list(request):
    s="""
    <br>
    <a href='/booktest/detail/1/'>跳转详细页1</a>
    <a href='/booktest/detail/2/'>跳转详细页2</a>
    <a href='/booktest/detail/3/'>跳转详细页3</a>

    
    """
    # return HttpResponse('这是列表页%s' %s)
    temp2=loader.get_template('booktest/list.html')
    books=BookInfo.objects.all()
    result=temp2.render({'book':books})

    return HttpResponse(result)


def detail(request,id):
    # return HttpResponse('这是详情页%s'"<a href='/booktest/'>跳转首页</a>%(id)")
    temp3=loader.get_template('booktest/detail.html')
    book=BookInfo.objects.get(pk=id)
    print(book)
    result=temp3.render({"book":book})
    return HttpResponse(result)


def deletehero(request,id):
    hero=HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    # return HttpResponse('删除成功')

    return redirect(reverse('booktest:detail',args=(bookid,)))

def addhero(request,id):
    book=BookInfo.objects.get(pk=id)
    if request.method=="GET":
    # return HttpResponse('成功')
        return render(request,"booktest/addhero.html",{'book':book})
    elif request.method == "POST":
        name = request.POST.get("username")
        content = request.POST.get("content")
        gender=request.POST.get("gender")
        hero = HeroInfo()
        hero.name = name
        hero.gender=gender
        hero.content = content
        hero.book = book
        hero.save()
        return redirect(reverse("booktest:detail",args=(id,)))

