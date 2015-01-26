# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0006_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='transactions',
            field=models.ManyToManyField(to='userbase.Transaction', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
