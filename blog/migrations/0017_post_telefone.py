# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20160824_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='telefone',
            field=models.IntegerField(blank=True, null=True, max_length=12),
        ),
    ]
