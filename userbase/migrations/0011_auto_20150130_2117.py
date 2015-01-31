# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_levels(apps, schema_editor):
    LevelUp = apps.get_model("userbase", "LevelUp")
    LevelUp(level=3, cost=20).save()
    LevelUp(level=2, cost=10).save()
    LevelUp(level=1, cost=5).save()

class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0010_levelup'),
    ]

    operations = [
        migrations.RunPython(load_levels)
    ]
