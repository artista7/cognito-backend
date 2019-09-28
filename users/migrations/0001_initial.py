# Generated by Django 2.2.4 on 2019-09-26 16:46

import django.contrib.auth.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atnp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='createdAt')),
                ('updatedAt', models.DateTimeField(auto_now=True, db_column='updatedAt')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atnp.College')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atnp.Company')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atnp.Student')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]