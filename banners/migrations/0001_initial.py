# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', model_utils.fields.StatusField(choices=[('banner_top_desktop', 'banner_top_desktop'), ('banner_top_tablet', 'banner_top_tablet'), ('banner_top_mobile', 'banner_top_mobile')], default='banner_top_desktop', max_length=100, no_check_for_status=True)),
                ('image', models.ImageField(null=True, upload_to='banner_images')),
            ],
        ),
    ]
