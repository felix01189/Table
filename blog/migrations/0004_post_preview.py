# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151205_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.CharField(default='', max_length=30),
        ),
    ]
