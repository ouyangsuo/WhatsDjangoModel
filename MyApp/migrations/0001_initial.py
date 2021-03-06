# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-22 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amoney', models.FloatField(default=100)),
                ('ano', models.CharField(max_length=10, unique=True)),
                ('apwd', models.CharField(default='111111', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20, unique=True)),
                ('bgender', models.NullBooleanField(default=None)),
                ('bage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20, unique=True)),
                ('gtype', models.CharField(max_length=10)),
                ('gprice', models.FloatField(default=0)),
                ('ginfo', models.TextField()),
                ('gbuyers', models.ManyToManyField(to='MyApp.Buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odatetime', models.DateTimeField(auto_now_add=True)),
                ('obuyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Buyer')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='abuyer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Buyer'),
        ),
    ]
