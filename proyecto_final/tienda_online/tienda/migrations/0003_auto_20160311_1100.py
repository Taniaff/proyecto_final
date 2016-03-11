# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_articulos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='articulo',
            field=models.ForeignKey(to='tienda.articulos', null=True),
        ),
    ]
