from django.shortcuts import render , get_object_or_404
from weblog.models import Weblog


def weblogs(request):
    weblogs= Weblog.objects.all()
    return render(request, 'weblogs.html' , {'weblogs':weblogs})

def weblog(request,weblog_id):
    weblog= get_object_or_404(Weblog, pk=weblog_id )
    return render(request, 'weblog.html', { 'weblog' : weblog})

def share(request , user_id):
    return render(request, 'share.html')

def commentPost(request , user_id , post_id):
    return render(request, 'comment.html' )

def commentGet(request , post_id):
    return render(request , 'commentshow.html' , {'commnets': commentGet})
# Create your views here.
