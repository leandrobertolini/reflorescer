# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160823_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='obs',
            field=models.TextField(null=True),
        ),
    ]
