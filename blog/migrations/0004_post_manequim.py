# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160823_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='manequim',
            field=models.CharField(default=1, max_length=1, choices=[('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande'), ('GG', 'Extra Grande')]),
            preserve_default=False,
        ),
    ]
