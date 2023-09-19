from django.shortcuts import render
from .models import Notice

# Create your views here.
def index(request):
    article_list = Notice.objects.all().order_by('-write_date')
    context = {'article_list': article_list}
    return render(request, 'board/index.html', context)