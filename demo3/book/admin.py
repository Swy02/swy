from django.contrib import admin
from .models import *
# Register your models here.
class HeroInline(admin.StackedInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [HeroInline]

admin.site.register(BookInfo,BookInfoAdmin)

class HeroAdmin(admin.ModelAdmin):
    list_display = ['name','content']
admin.site.register(HeroInfo,HeroAdmin)


