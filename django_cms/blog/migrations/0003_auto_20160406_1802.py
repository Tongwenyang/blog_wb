# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160406_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='deleted',
            field=models.BooleanField(verbose_name='删除', default=False),
        ),
        migrations.AddField(
            model_name='column',
            name='deleted',
            field=models.BooleanField(verbose_name='删除', default=False),
        ),
        migrations.AddField(
            model_name='column',
            name='important_num',
            field=models.IntegerField(verbose_name='优先级', default=0),
        ),
    ]
