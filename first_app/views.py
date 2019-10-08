from django.shortcuts import render
from django.http import HttpResponse
#对应第七点
from .models import Article
# Create your views here.
def article_detail(request,article_id):
    article=Article.objects.get(id=article_id)
    return HttpResponse("文章id为：%s" % article_id)