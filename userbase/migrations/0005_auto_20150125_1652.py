# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0004_auto_20150123_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='userOther',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='userThis',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='withdraw',
        ),
    ]
