from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag


from post.models import Post


def get_all_posts(request, id_list=None):
    categories = Tag.objects.all()
    if id_list:
        posts = Post.objects.filter(pk__in=id_list).order_by('-datetime')
    else:
        posts = Post.objects.all().order_by('-datetime')
    num_items = request.GET.get('num_items', 3)
    paginator = Paginator(posts, num_items)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context = {'posts': posts, 'num_items': num_items, 'categories': categories}
    return render(request, 'post/index.html', context=context)


def get_single_post(request, post_id):
    categories = Tag.objects.all()
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post,  'categories': categories}
    return render(request, 'post/single_post.html', context=context)
