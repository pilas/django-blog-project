# Create your views here.

from django.shortcuts import render_to_response
from models import Post, Comment


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return render_to_response('list/post_list.html',{'post_list':post_list})

def post_detail(request, id, showComments=False):
    post_list = Post.objects.all()	
    pid = Post.objects.get(pk=id)
    comment = Comment.objects.all()
    comid = Comment.objects.get(pk=id)
    relation = pid.comments.all()
    return render_to_response('list/post_detail.html',{'pid':pid,'post_list':post_list,'comment':comment,'comid':comid,'relation':relation})
    
def post_search(request, term):
    postser = Post.objects.filter(title__contains=term)
    return render_to_response('list/post_search.html',{'postser':postser,'term':term})
def home(request):
    print 'it works'
    return render_to_response('hello world. Ete zene?',locals()) 
