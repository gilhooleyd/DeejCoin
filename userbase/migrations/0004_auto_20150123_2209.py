# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0003_auto_20150123_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='user',
            new_name='userThis',
        ),
        migrations.AddField(
            model_name='transaction',
            name='userOther',
            field=models.CharField(default='WOOBLOO', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='withdraw',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
