# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='telefone',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
