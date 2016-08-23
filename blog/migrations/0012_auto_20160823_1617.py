# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160823_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='responsavel',
        ),
    ]
