from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404


# TODO add views for searching
from django.utils import timezone

from post.models import Post, Comments, Replies


def get_all_posts(request):
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
    context = {'posts': posts, 'num_items': num_items}
    return render(request, 'post/index.html', context=context)


def get_single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post/single_post.html', context=context)


def post_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        author = request.POST.get('author', None)
        datetime = timezone.now()
        content = request.POST.get('content')
        new_comment = Comments(post=post, author=author, datetime=datetime, content=content)
        new_comment.save()
        return JsonResponse({'content': str(content)})
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return HttpResponseRedirect('http://127.0.0.1:8000/post/'+str(post.id)+'/', context)


def post_reply(request, comment_id):
    if request.method == 'POST':
        comment = Comments.objects.get(pk=comment_id)
        author = request.POST.get('author', None)
        datetime = timezone.now()
        content = request.POST.get('content')
        new_reply = Replies(comment=comment, author=author, datetime=datetime, content=content)
        new_reply.save()
    post = get_object_or_404(Post, pk=Comments.objects.get(pk=comment_id).post.id)
    context = {'post': post}
    return HttpResponseRedirect('http://127.0.0.1:8000/post/'+str(post.id)+'/', context)
