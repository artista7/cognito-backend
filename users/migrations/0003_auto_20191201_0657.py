# Generated by Django 2.2.5 on 2019-12-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191011_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
