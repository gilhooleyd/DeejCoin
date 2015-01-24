# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0002_auto_20150122_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(to='userbase.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_coins',
            new_name='coins',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_nick',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_status',
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
