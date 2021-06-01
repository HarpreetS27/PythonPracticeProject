from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def index(request):
    allpost=Blogpost.objects.all()
    return render(request,'BlogSite/index.html',{'allpost':allpost})


def blogPost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]

    return render(request,'BlogSite/blogPost.html',{'post':post})