# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(blank=True, null=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pagamento',
            field=models.CharField(max_length=20, choices=[('Em Aberto', 'Em Aberto'), ('Total', 'Total'), ('Carteirinha', 'Carteirinha'), ('Fantasia', 'Fantasia')]),
        ),
    ]
