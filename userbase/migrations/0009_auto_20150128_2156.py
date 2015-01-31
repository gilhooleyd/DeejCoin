# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='message',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
