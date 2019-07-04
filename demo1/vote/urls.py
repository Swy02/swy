
from django.conf.urls import url
from .import views
app_name='vote'
urlpatterns = [

    url(r'^index/$',views.index,name='index/index.html'),
]