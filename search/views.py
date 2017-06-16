from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from post import views as post_views


def search(request):
    print(request.GET)
    keyword = request.GET.get("keyword", "post")
    es_client = Elasticsearch()
    result_set = Search(using=es_client, index="blog", )\
        .query("match", content=keyword)
    response = result_set.execute()
    id_list = get_id_from_response(response)
    return post_views.get_all_posts(request, id_list)


def get_id_from_response(response):
    id_list = []
    for hit in response:
        id_list.append(hit.meta.id)
    return id_list
