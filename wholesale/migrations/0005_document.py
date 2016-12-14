# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0004_remove_order_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('Cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wholesale.Customer')),
            ],
        ),
    ]
