# Generated by Django 2.2.5 on 2019-09-30 19:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='userName',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='aboutMe',
        ),
        migrations.AddField(
            model_name='student',
            name='profileInfo',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column='profileInfo', null=True),
        ),
    ]
