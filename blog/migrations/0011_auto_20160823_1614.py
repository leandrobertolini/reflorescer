# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160823_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='manequim',
            field=models.CharField(choices=[('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande'), ('GG', 'Extra Grande')], max_length=2),
        ),
    ]
