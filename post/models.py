import os
import zipfile

from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
import imagekit.processors

from post import image_resizer


class Post(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    title = models.CharField(max_length=100)
    title_image = models.ImageField(upload_to='title_images/', null=True, blank=True)
    one_line_description = models.CharField(max_length=200)
    resized_title_image = ImageSpecField(source='title_image',
                                         processors=[imagekit.processors.resize.ResizeToFit(900, 300)],
                                         format='JPEG',
                                         options={'quality': 60})
    author = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=1150000)
    content_zip = models.FileField(upload_to='zip', blank=True, null=True)
    categories = TaggableManager()
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def indexing(self):
        from .elasticsearch_operations import PostIndex
        obj = PostIndex(
            meta={'id': self.id},
            author=self.author,
            title=self.title,
            content=self.content,
            categories=self.get_category()
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    def delete_post_from_elasticsearch(self):
        from elasticsearch_operations import delete_post
        delete_post(self.id)

    def save(self, *args, **kwargs):
        if self.content_zip:
            content_folder = settings.MEDIA_ROOT + '/content_files/'+self.title + '/'
            img_folder = content_folder + 'img/'
            resized_img_folder = content_folder + 'resized_img/'
            if not os.path.exists(os.path.dirname(content_folder)):
                    os.makedirs(os.path.dirname(content_folder))
            content_zip = zipfile.ZipFile(self.content_zip)
            zipfile.ZipFile.extractall(content_zip, path=content_folder)
            if not os.path.exists(os.path.dirname(img_folder)):
                raise NotImplementedError(img_folder+'not found in zip file')
            if not os.path.exists(os.path.dirname(resized_img_folder)):
                os.makedirs(os.path.dirname(resized_img_folder))
            img_files = os.listdir(img_folder)
            for img_file in img_files:
                source = img_folder + img_file
                destination = resized_img_folder + 'resized_' + img_file
                image_resizer.ResizeImage.resize_and_save_image(source=source, destination=destination)
        super(Post, self).save(*args, **kwargs)

    def get_category(self):
        category_str = ""
        for i in self.categories.iterator():
            category_str = category_str + ' , ' + str(i)
        return category_str
