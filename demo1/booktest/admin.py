from django.contrib import admin
from .models import *
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title']



admin.site.register(BookInfo,BookInfoAdmin)



class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['name','content']


admin.site.register(HeroInfo,HeroInfoAdmin)