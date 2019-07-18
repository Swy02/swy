from django.conf.urls import url
from . import views
from .views import *

app_name='robot'

urlpatterns = [
    url('^$',views.IndexView.as_view(),name='index'),
    url('^about_us/$',views.About_us.as_view(),name='about_us'),
    url('^news/$', views.NewsView.as_view(), name='news'),
    url('^baoming/$', views.BaoMing.as_view(), name='baoming'),
    url('^competition/$', views.Competition.as_view(), name='competition'),
    url('^teachers_team/$', views.Teachers_team.as_view(), name='teachers_team'),
    url('^class_sys/$', views.Class_sys.as_view(), name='class_sys'),
    url('^classroom_show/$', views.Classroom_show.as_view(), name='classroom_show'),
    url('^contact_us/$', views.Contact_us.as_view(), name='contact_us'),
    url('^detail/(\d+)/$', views.Detail.as_view(), name='detail'),
    url('^detail1/(\d+)/$', views.Detail1.as_view(), name='detail1'),


]