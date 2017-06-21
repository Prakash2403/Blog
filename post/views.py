from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from post.models import Post


def get_all_posts(request):
    categories = Tag.objects.all()
    posts = Post.objects.all().filter(draft=False).order_by('-datetime')
    page = request.GET.get('page')
    num_items = request.GET.get('num_items', 3)
    posts = paginate_post(page=page, posts=posts, num_items=num_items)
    context = {'posts': posts, 'num_items': num_items, 'categories': categories}
    return render(request, 'post/index.html', context=context)


def get_single_post(request, post_id):
    categories = Tag.objects.all()
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post,  'categories': categories}
    return render(request, 'post/single_post.html', context=context)


def get_search_results(request, id_list):
    categories = Tag.objects.all()
    domain = request.GET.get('domain')
    keyword = request.GET.get('keyword')
    page = request.GET.get('page')
    posts = Post.objects.all().filter(draft=False).filter(pk__in=id_list).order_by('-datetime')
    num_items = request.GET.get('num_items', 3)
    posts = paginate_post(page=page, posts=posts, num_items=num_items)
    context = {'posts': posts, 'num_items': num_items, 'categories': categories, 'keyword': keyword, 'domain': domain}
    return render(request, 'post/index.html', context=context)


def paginate_post(page, posts, num_items):
    paginator = Paginator(posts, num_items)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return posts