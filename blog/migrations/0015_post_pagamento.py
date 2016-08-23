# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_delete_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pagamento',
            field=models.CharField(default=1, max_length=20, choices=[('Total', 'Total'), ('Carteirinha', 'Carteirinha'), ('Fantasia', 'Fantasia')]),
            preserve_default=False,
        ),
    ]
