# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-14 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('article_date', models.DateTimeField()),
                ('article_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('comments_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
