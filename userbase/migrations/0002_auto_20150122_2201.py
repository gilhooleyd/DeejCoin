# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_nick',
            field=models.CharField(default='new-user', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.CharField(default='just joined!', max_length=1000),
            preserve_default=True,
        ),
    ]
