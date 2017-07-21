# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('title_image', models.ImageField(blank=True, null=True, upload_to=b'title_images/')),
                ('author', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(max_length=10000)),
                ('content_zip', models.FileField(blank=True, null=True, upload_to=b'zip')),
                ('quote', models.TextField(default=b'Stay hungry, Stay foolish', max_length=400)),
                ('quoted_by', models.CharField(default=b'Steve Jobs', max_length=30)),
                ('draft', models.BooleanField(default=True)),
                ('categories', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
