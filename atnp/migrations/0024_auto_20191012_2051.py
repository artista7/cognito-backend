# Generated by Django 2.2.5 on 2019-10-12 20:51

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0023_auto_20191012_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeopening',
            name='commentJson',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, default=list, null=True, size=None),
        ),
    ]
