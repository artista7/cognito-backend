# Generated by Django 2.2.5 on 2019-10-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0029_auto_20191018_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(db_column='name', default='Vivek', max_length=2000),
            preserve_default=False,
        ),
    ]
