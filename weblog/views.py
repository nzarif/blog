from django.shortcuts import render , get_object_or_404
from weblog.models import Weblog, Comment, Post


def weblogs(request):
    webloglist= Weblog.objects.all()
    return render(request, 'weblogs.html', {'weblogs': webloglist})


def weblog(request, weblog_id):
    weblog= get_object_or_404(Weblog, pk=weblog_id )
    return render(request, 'weblog.html', {'weblog': weblog})


def share(request, user_id):
    return render(request, 'share.html')


def comment(request, user_id, post_id):
    return render(request, 'comment.html' )


def comments(request, post_id):
    comment = Comment.objects.all().filter(pk=post_id)
    return render(request, 'commentshow.html', {'commnets': comment})


def posts(request, user_id):
    posts=Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post(request,post_id):
    post = get_object_or_404( Post , pk=post_id)
    return render(request , 'post.html', post)
