# Generated by Django 2.2.5 on 2019-10-02 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0003_auto_20191002_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentindrive',
            name='student',
            field=models.ForeignKey(blank=True, db_column='student', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='atnp.Student'),
        ),
    ]
