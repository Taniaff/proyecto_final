# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('caracteristicas', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200)),
                ('articulo', models.ForeignKey(to='tienda.articulos')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='linea',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('cod_articulo', models.ForeignKey(to='tienda.articulos')),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('fecha_pedido', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('direccion_entrega', models.CharField(max_length=50)),
                ('autor_pedido', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='linea',
            name='cod_pedido',
            field=models.ForeignKey(to='tienda.pedido'),
        ),
        migrations.AlterUniqueTogether(
            name='linea',
            unique_together=set([('cod_pedido', 'cod_articulo')]),
        ),
    ]
