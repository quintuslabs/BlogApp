from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

def home(request):
    return render(request,"article/index.html",{"name":"Santosh"})

def articles(request):
    articles = Article.objects.all()
    return render(request,"article/articles.html",{"articles":articles})

def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)
        
        # article.author = request.user
        article.save()

        messages.success(request,"Article Successfully Added!!!")
        return redirect("article:articles")
    return render(request,"article/addarticle.html",{"form":form})
    
def updateArticle(request,id):    
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        # article.author = request.user
        article.save()

        messages.success(request,"Article Successfully Updated")
        return redirect("article:articles")


    return render(request,"article/update.html",{"form":form})
    
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Article Successfully Deleted!!")
    return redirect("article:articles")