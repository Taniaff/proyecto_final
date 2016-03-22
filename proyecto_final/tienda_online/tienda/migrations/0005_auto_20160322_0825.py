# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20160311_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
