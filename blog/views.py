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
    Post.objects.filter(id=nothing_num).update(hits = boardData.hits + 1)
    return render(request, 'blog/viewMemo.html', {'memo_id': nothing_num, 'boardData': boardData})

@csrf_exempt
def DoWriteBoard(request):
    te=request.POST['memo']
    previ=te[0:30]
    br = Post(title = request.POST['subject'], writer = request.POST['name'], text = request.POST['memo'], created_date = timezone.now(), preview = previ)
    br.save()
    url = '/post_list'
    return HttpResponseRedirect(url)

@csrf_exempt
def search(request):
    search_word = request.POST['searching']
    searchCnt = Post.objects.filter(title__contains=search_word).count()
    boardList = Post.objects.filter(title__contains=search_word).order_by('-id')[0:searchCnt]
    return render(request, 'blog/search.html', {'boardList': boardList, 'searchCnt': searchCnt, 'search_word': search_word})
