# Generated by Django 2.2.5 on 2019-10-05 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0014_auto_20191005_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='canDelete',
            field=models.BooleanField(blank=True, db_column='canDelete', null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='canEdit',
            field=models.BooleanField(blank=True, db_column='canEdit', null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='isInterview',
            field=models.BooleanField(blank=True, db_column='isInterview', null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='jobOpening',
            field=models.ForeignKey(db_column='jobOpening', on_delete=django.db.models.deletion.DO_NOTHING, related_name='rounds', to='atnp.JobOpening'),
        ),
    ]