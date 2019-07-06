from django.conf.urls import url
from . import views
app_name='book'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^addhero/(\d+)/$', views.addHero, name='addhero'),
    url(r'^deletehero/(\d+)/$', views.deleteHero, name='deletehero')

]