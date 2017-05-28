from django.shortcuts import render, get_object_or_404


# TODO add views for searching
from post.models import Post


def index(request):
    post = get_object_or_404(Post, pk=1)
    context = {'post': post}
    return render(request, 'post/index.html', context=context)