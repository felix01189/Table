# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]
