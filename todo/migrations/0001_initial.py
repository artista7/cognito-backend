# Generated by Django 2.2.5 on 2019-10-17 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task', models.CharField(db_column='message', max_length=2000)),
                ('status', models.CharField(db_column='status', max_length=255)),
                ('category', models.CharField(db_column='category', max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='createdAt')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'todo',
            },
        ),
    ]