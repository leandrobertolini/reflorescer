# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_pagamento'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pagamento',
        ),
    ]
