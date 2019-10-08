from django.shortcuts import render
from django.http import HttpResponse
#对应第七点
from .models import Article
# Create your views here.
def article_detail(request,article_id):
    article=Article.objects.get(id=article_id)
    #显示数据库中保存的文章标题和内容
    return HttpResponse("文章标题：%s<br>文章内容：%s" % (article.title,article.intend))
    #return HttpResponse("文章id为：%s" % article_id)