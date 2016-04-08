# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160406_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=50, verbose_name='描述', default=datetime.datetime(2016, 4, 8, 17, 38, 35, 252490, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
