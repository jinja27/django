from django.contrib import admin
from .models import Article
# Register your models here.
#在后台可以管理我们的模板
admin.site.register(Article)