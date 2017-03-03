# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20170303_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('user', models.ForeignKey(related_name='tags', verbose_name='user', to='taskmanager.Profile')),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'verbose_name': 'Tag',
                'ordering': ('user', 'name'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('user', 'name')]),
        ),
    ]
