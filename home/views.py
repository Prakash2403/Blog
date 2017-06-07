from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from post.models import Post


def index(request, id_list=None):
    if id_list is None:
        posts = Post.objects.all().order_by('-datetime')
    else:
        posts = Post.objects.filter(pk__in=id_list)
    num_items = request.GET.get('num_items', 3)
    paginator = Paginator(posts, num_items)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context = {'posts': posts, 'num_items': num_items}
    return render(request, 'home/index.html', context=context)
