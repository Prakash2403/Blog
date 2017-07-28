from django.http import Http404
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from post.models import Post
from utils import paginate_post


def get_all_posts(request):
    categories = Tag.objects.all()
    posts = Post.objects.all().filter(draft=False).order_by('-datetime')
    page = request.GET.get('page')
    num_items = request.GET.get('num_items', 9)
    posts = paginate_post(page=page, posts=posts, num_items=num_items)
    context = {'posts': posts, 'num_items': num_items, 'categories': categories}
    return render(request, 'post/index.html', context=context)


def get_single_post(request, post_id):
    categories = Tag.objects.all()
    post = get_object_or_404(Post, pk=post_id)
    if post.draft:
        raise Http404
    context = {'post': post,  'categories': categories}
    return render(request, 'post/single_post.html', context=context)


def get_search_results(request, id_list):
    categories = Tag.objects.all()
    page = request.GET.get('page')
    posts = Post.objects.all().filter(draft=False).filter(pk__in=id_list)
    num_items = 9
    posts = paginate_post(page=page, posts=posts, num_items=num_items)
    context = {'posts': posts, 'num_items': num_items,
               'categories': categories, 'keyword': request.GET.get('keyword'),
               'domain': request.GET.get('domain')}
    return render(request, 'post/index.html', context=context)
