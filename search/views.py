from elasticsearch_dsl import Search

from post import views as post_views
from search.helpers import search_keyword, \
    get_id_from_response, \
    get_suggested_id_from_response, get_search_object


def search(request):
    domain = request.GET.get('domain')
    if domain == 'post':
        return search_in_post(request)
    elif domain == 'category':
        return search_in_category(request)


def search_in_post(request):
    keyword = request.GET.get("keyword")
    response = search_keyword(keyword)
    id_list = get_id_from_response(response)
    suggested_id_list = get_suggested_id_from_response(response.suggest.post_suggester)
    for suggested_id in suggested_id_list:
        for id in suggested_id:
            id_list.append(id)
    return post_views.get_search_results(request, id_list)


def search_in_category(request):
    keyword = request.GET.get("keyword")
    es_client = get_search_object()
    result_set = Search(using=es_client, index="blog").\
        query("match", categories=keyword)
    response = result_set.execute()
    id_list = get_id_from_response(response)
    return post_views.get_search_results(request, id_list)
