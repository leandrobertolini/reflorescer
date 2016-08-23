# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160823_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='obs',
        ),
        migrations.AddField(
            model_name='post',
            name='calcado',
            field=models.CharField(max_length=2, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='cidade',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='roupa',
            field=models.CharField(max_length=2, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]
