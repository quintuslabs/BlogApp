from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

def home(request):
    return render(request,"article/index.html",{"name":"Santosh"})
