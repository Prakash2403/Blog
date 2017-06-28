import calendar
import datetime
from collections import OrderedDict

from django.shortcuts import render, get_object_or_404

# Create your views here.
from post.models import Post


def index(request):
    posts = Post.objects.all().order_by('-datetime')
    curr_year = datetime.datetime.now().year
    start_year = 2015
    archive_posts = OrderedDict()
    for year in range(curr_year, start_year, -1):
        archive_post_year = OrderedDict()
        for i in range(12, 0, -1):
            post = posts.filter(datetime__month=i).filter(datetime__year=year).filter(draft=False)
            if post:
                archive_post_year[str(calendar.month_name[i])] = post
        archive_posts[str(year)] = archive_post_year
    context = {'archive_posts': archive_posts}
    return render(request, 'archive/index.html', context=context)
