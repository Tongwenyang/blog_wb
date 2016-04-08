# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发表时间', auto_now_add=True, default=datetime.datetime(2016, 4, 6, 15, 5, 28, 266637, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(null=True, verbose_name='更新时间', auto_now=True),
        ),
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(verbose_name='首页显示', default=False),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(verbose_name='导航显示', default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容', blank=True, default=''),
        ),
    ]
