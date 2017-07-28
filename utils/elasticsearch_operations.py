from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
import post.models

connections.create_connection()


def bulk_indexing():
    PostIndex.init("post")
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in post.models.Post.objects.all().iterator()))


def delete_post(post_id):
    es = Elasticsearch()
    es.delete(index='blog', doc_type="post_index", id=post_id, refresh=True)


class PostIndex(DocType):
    title = Text()
    author = Text()
    content = Text()
    categories = Text()

    class Meta:
        index = 'blog'
