# Generated by Django 2.2.5 on 2019-10-02 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0009_auto_20191002_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeopening',
            name='studentInDrive',
            field=models.ForeignKey(db_column='studentInDrive', on_delete=django.db.models.deletion.DO_NOTHING, related_name='resumeOpenings', to='atnp.StudentInDrive'),
        ),
    ]
