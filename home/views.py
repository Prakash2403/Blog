from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from post.models import Post


def index(request, id_list=None):
    if id_list is None:
        posts = Post.objects.all()
        print(posts)
        context = {'posts': posts}
        return render(request, 'home/index.html', context=context)
    else:
        posts = Post.objects.filter(pk__in=id_list)
        context = {'posts': posts}
        return render(request, 'home/index.html', context=context)
