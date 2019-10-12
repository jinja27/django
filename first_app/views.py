from django.shortcuts import render,render_to_response
from django.http import HttpResponse
#对应第七点
from .models import Article
# Create your views here.
def article_detail(request,article_id):
    article=Article.objects.get(id=article_id)
    context={}
    #context是一个字典，我们定义了一个参数article_obj，意思是在字典context中，键article_obj对应的值为通过obj.get获取到的值（/1，/2等）。
    context['article_obj']=article
    return render(request,"article_html.html",context)
    #显示数据库中保存的文章标题和内容
    #为了分离前后端代码而注释
    #return HttpResponse("<h2>文章标题：%s</h2><br>文章内容：%s" % (article.title,article.intend))
    #return HttpResponse("文章id为：%s" % article_id)


def article_list(request):
    article111=Article.objects.all()
    context={}
    context['articles']=article111
    return render_to_response("article_list.html",context)