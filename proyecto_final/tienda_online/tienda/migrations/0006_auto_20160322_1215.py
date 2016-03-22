# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_auto_20160322_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='autor_pedido',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
