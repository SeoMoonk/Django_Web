from django.shortcuts import render, redirect
from .models import Notice
from django.urls import reverse

# Create your views here.
def index(request):
    article_list = Notice.objects.all().order_by('-write_date')
    context = {'article_list': article_list}
    return render(request, 'board/index.html', context)


def write_article(request):
    return render(request, 'board/write.html')

def add(request):
    notice = Notice()
    notice.title = request.POST['i_title']
    notice.content = request.POST['i_content']
    notice.write_id = 'TestUser01'
    notice.save()

    return redirect(reverse('board:index'))