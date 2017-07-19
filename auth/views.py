from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from weblog.models import Weblog
from auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse



@csrf_exempt
def login(request):
    if request.method == 'POST':
        use = request.POST['username']
        pas = request.POST['password']
        try:
            user = User.objects.get(username=use, password=pas)
        except User.DoesNotExist:
            user = None
        if (user != None):
            import uuid
            token = uuid.uuid4().hex
            user.token = token
            user.save()
            return JsonResponse({'status': 0, 'token': token})
        else:
            return JsonResponse({'status': -1})
    else:
        return HttpResponse("login")



    def blogId(request):
        token = request.META['HTTP_X_TOKEN']
        try:
            user = MyUser.objects.get(token=token)
        except MyUser.DoesNotExist:
            user = None
        if user != None:
            return JsonResponse({'status': 0, 'blog-id': user.blog_id})
        else:
            return JsonResponse({'status': -1})


@csrf_exempt
def register(request):
    bid = 0
    try:
        i = Weblog.objects.count()
        bid = Weblog.objects.all()[i - 1].bid
    except:
        bid = 0
    if request.method == 'POST':
        mail = None
        first = None
        last = None
        use = request.POST['username']
        pas = request.POST['password']
        if 'email' in request.POST:
            mail = request.POST['email']
        if 'first_name' in request.POST:
            first = request.POST['first_name']
        if 'last_name' in request.POST:
            last = request.POST['last_name']
        user = User.objects.create(username=use, password=pas, firstName=first, lastName=last, email=mail)
        Weblog.objects.create(bid=bid, author=user)
        user.bid = bid
        user.save()
        return JsonResponse({'status': 0})
    return render(request , 'login.html')