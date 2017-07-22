from django.http import JsonResponse
from authc.models import User
from weblog.models import Weblog
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



def bid(request):
    t = request.META['HTTP_X_TOKEN']
    try:
        u = User.objects.get(token=t)
    except User.DoesNotExist:
        u = None
    if u == None:
        return JsonResponse({'status': -1})
    else:
        return JsonResponse({'status': 0, 'bid': u.bid})


@csrf_exempt
def register(request):
    if request.method == 'GET':
        return HttpResponse("wrong method for registering")
    else:
        try:
            i= Weblog.objects.count()
            bid = Weblog.objects.all()[i - 1].id
            bid=bid+1
        except:
            bid = 0
        use = request.POST['username']
        pas = request.POST['password']
        if 'email' in request.POST:
            mail = request.POST['email']
        else:
            mail= None
        if 'first_name' in request.POST:
            first = request.POST['first_name']
        else:
            first = None
        if 'last_name' in request.POST:
            last = request.POST['last_name']
        else:
            last = None
        u = User.objects.create(username=use, password=pas, firstName=first, lastName=last, email=mail)
        Weblog.objects.create(id=bid,author=u)
        u.save()
        return JsonResponse({'status': 0 , 'bid':bid})


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return HttpResponse("login")
    else:
        use = request.POST['username']
        pas = request.POST['password']
        try:
            u = User.objects.get(username=use, password=pas)
        except User.DoesNotExist:
            u = None
        if u == None:
            return JsonResponse({'status': -1})
        else:
            import uuid
            t = uuid.uuid4().hex
            u.token = t
            u.save()
            return JsonResponse({'status': 0, 'token': t})

