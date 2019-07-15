import xadmin
from .models import *
from django.contrib import admin
admin.ModelAdmin
xadmin.site.register(Category)
xadmin.site.register(Tag)

class ArticleAdmin:
    # 模型字段想要用ueditor样式重新注册模型管理类
    style_fields = {"body": "ueditor"}

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ads)