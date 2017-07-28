from post.models import Post
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=Post)
def index_post(sender, instance, **kwargs):
    instance.indexing()


@receiver(post_delete, sender=Post)
def delete_post(sender, instance, **kwargs ):
    instance.delete_post_from_elasticsearch()
