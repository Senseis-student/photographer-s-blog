from django.shortcuts import render
from django.db import models
from django.shortcuts import redirect
from . import models


def blog(request):
    post_list = models.Post.objects.all()
    return render(request, 'blog/blog.html', {'post_list': post_list})

def view_post(request, post_id):
    post = models.Post.objects.get(id=post_id)
    post_list = models.Post.objects.exclude(id=post_id).order_by('-id')[0:4]
    comments = models.Comment.objects.filter(post = post).order_by('-id')
    return render(request, 'blog/post.html',{'post':post,'post_list':post_list,'comments':comments})

def add_new_comment(request, post_id):
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        a = models.Comment()
        a.post = models.Post.objects.get(id= post_id)
        a.author = author
        a.textComment = text
        if a.textComment!='':
            if a.author!='':
                a.save()
    return redirect ('view_post', post_id=post_id)
