from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate_post(page, posts, num_items):
    paginator = Paginator(posts, num_items)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return posts
