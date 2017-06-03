from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from home import views as home_views


def search(request):
    keyword = request.GET.get("keyword", "post")
    es_client = Elasticsearch()
    result_set = Search(using=es_client, index="blog", )\
        .query("match", content=keyword)
    response = result_set.execute()
    id_list = get_id_from_response(response)
    return home_views.index(request, id_list)


def get_id_from_response(response):
    id_list = []
    for hit in response:
        id_list.append(hit.meta.id)
    return id_list
