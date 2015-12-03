from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def post_list(request):
    totalCnt = Post.objects.all().count()
    boardList = Post.objects.order_by('-id')[0:totalCnt]
    return render(request, 'blog/post_list.html', {'boardList': boardList, 'totalCnt': totalCnt})

def show_write_form(request):
    return render(request, 'blog/show_write_form.html')

@csrf_exempt
def showpage(request):
    pk = request.GET['memo_id']
    nothing_num=0
    nothing_len=len(pk)-6
    for i in range(nothing_len):
        nothing_num=nothing_num*10+int(pk[i])
    boardData = Post.objects.get(id=nothing_num)
    return render(request, 'blog/viewMemo.html', {'memo_id': nothing_num, 'boardData': boardData } )

@csrf_exempt
def DoWriteBoard(request):
    br = Post(title = request.POST['subject'], writer = request.POST['name'], text = request.POST['memo'], created_date = timezone.now())
    br.save()
    url = '/post_list'
    return HttpResponseRedirect(url)


def register(request):
    from blog.models import Post
    from django.contrib.auth.models import User
    User.objects.create_user(request.POST.get['username'],request.POST.get['mail'],request.POST.get['password'])
    return
