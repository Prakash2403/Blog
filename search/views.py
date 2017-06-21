from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from post import views as post_views


def search(request):
    domain = request.GET.get('domain')
    if domain == 'post':
        return search_in_post(request)
    elif domain == 'category':
        return search_in_category(request)


def search_in_post(request):
    keyword = request.GET.get("keyword")
    es_client = Elasticsearch()
    result_set = Search(using=es_client, index="blog", )\
        .query("match", content=keyword)
    response = result_set.execute()
    id_list = get_id_from_response(response)
    return post_views.get_search_results(request, id_list)


def search_in_category(request):
    keyword = request.GET.get("keyword")
    es_client = Elasticsearch()
    result_set = Search(using=es_client, index="blog").\
        query("match", categories=keyword)
    response = result_set.execute()
    id_list = get_id_from_response(response)
    return post_views.get_search_results(request, id_list)


def get_id_from_response(response):
    id_list = []
    for hit in response:
        id_list.append(hit.meta.id)
    return id_list
