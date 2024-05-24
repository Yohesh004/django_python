from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    blog_title="Yogi posts"
    posts = [
        {'id':1,'title': 'Post1','content':'content of post1'},
        {'id':2,'title': 'Post2','content':'content of post2'},
        {'id':3,'title': 'Post3','content':'content of post3'},
        {'id':4,'title': 'Post4','content':'content of post4'},

        
    ]
    return render(request,'index.html',{'blog_title':blog_title, 'posts':posts})
def detail(request,post_id):
    return render(request,'detail.html')
def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_view(request):
    return HttpResponse("this is the new url")
