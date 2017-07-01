from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


def get_search_object():
    es_client = Elasticsearch()
    search_object = Search(using=es_client, index="blog")
    return search_object


def get_id_from_response(response):
    id_list = []
    for hit in response:
        id_list.append(hit.meta.id)
    return id_list


def get_suggested_id_from_response(suggest_obj):
    approximate_id_list = []
    for obj in suggest_obj:
        for option in obj['options']:
            approximate_id_list.append\
                (get_id_from_response(search_keyword(option['text'])))
    return approximate_id_list


def search_keyword(keyword):
    result_set = get_search_object().query("match", title=keyword) \
        .suggest("post_suggester", keyword, term={'field': 'title'})
    return result_set.execute()
