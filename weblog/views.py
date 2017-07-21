from weblog.models import Post, Weblog, Comment
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def share(request, bid):
    bid=int(bid)
    try:
        t = request.META['HTTP_X_TOKEN']
    except:
        t = None
    if request.method == 'GET':
        return JsonResponse({'status': -1})
    elif t == None:
        return JsonResponse({'status': -1})
    else:
        ttl = request.POST['title']
        summ = request.POST['summary']
        txt = request.POST['text']
        try:
            w = Weblog.objects.get(id=bid, author__token=t)
        except:
            w=None
        if w == None:
            return JsonResponse({'status': -1, 'msg':"no such weblog" ,'bid':bid , 'token':t})
        else:
            try:
                i = Post.objects.count()
                pid = Post.objects.all()[i - 1].id
            except:
                pid = 0
            import datetime
            Post.objects.create(weblog=w, id=pid + 1, title=ttl, summary=summ, text=txt, date=datetime.datetime.now())
            return JsonResponse({'status': 0 , 'pid':pid+1})



@csrf_exempt
def getposts(request, bid):
    bid = int(bid)
    if request.method == 'POST':
        return HttpResponse("wrong method for posts")
    else:
        try:
            t = request.META['HTTP_X_TOKEN']
        except:
            t = None
        if t == None:
            JsonResponse({'status': -1})
        else:
            offst = 0
            cnt = 5
            if 'count' in request.GET:
                tmp = request.GET['count']
                cnt = int(tmp)
            if 'offset' in request.GET:
                tmp=request.GET['offset']
                offst = int(tmp)
            try:
                p = Post.objects.filter(weblog__author__token=t, weblog__id=bid)
                if len(p) < cnt:
                    cnt = len(p)
                p = p[offst:offst + cnt]
            except:
                p = None
            if p == None:
                return JsonResponse({'sattus': -1})
            else:
                parray = []
                for pst in p:
                    parray.append({'id': pst.id, 'title': pst.title, 'summary': pst.summary, 'datetime': pst.date})
                psts = {'status': 0, 'posts': parray}
                return JsonResponse(psts)





@csrf_exempt
def comment(request, bid):
    bid = int(bid)
    try:
        t = request.META['HTTP_X_TOKEN']
    except:
        t = None
    if request.method == 'GET':
        return JsonResponse({'status': -1})
    elif t == None:
        return JsonResponse({'status': -1})
    else:
        txt = request.POST['text']
        pid = int(request.POST['post_id'])
        try:
            p = Post.objects.get(id=pid, weblog__author__token=t, weblog__id=bid)
        except:
            p = None
        if p == None:
            return JsonResponse({'status': -1})
        try:
            i = Comment.objects.count()
            cid = Comment.objects.all()[i - 1].id
        except:
            cid = 0
        import datetime
        Comment.objects.create(pid=p, id=cid + 1, text=txt, date=datetime.datetime.now())
        return JsonResponse({'status': 0})



@csrf_exempt
def getcomments(request, bid):
    bid = int(bid)
    if request.method == 'POST':
        return HttpResponse("posts")
    else:
        try:
            t = request.META['HTTP_X_TOKEN']
        except:
            t = None
        if t == None:
            JsonResponse({'status': -1})
        else:
            offst = 0
            cnt = 5
            if 'offset' in request.GET:
                offst = int(request.GET['offset'])
            if 'count' in request.GET:
                cnt = int(request.GET['count'])
            try:
                cms = Comment.objects.filter(post__weblog__author__token=t , post__weblog__id=bid)
                if len(cms) < cnt:
                    cnt = len(cms)
                cms = cms[offst:offst + cnt]
            except:
                cms = None
            if cms == None:
                return JsonResponse({'sattus': -1 })
            else:
                cmarray = []
                for comnt in cms:
                    cmarray.append({'text': comnt.text, 'datetime': comnt.date})
                comnts = {'status': 0, 'comments': cmarray}
                return JsonResponse(comnts)


