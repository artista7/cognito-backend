# Generated by Django 2.2.5 on 2019-10-02 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0008_auto_20191002_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeopening',
            name='studentInDrive',
            field=models.ForeignKey(db_column='studentInDrive', on_delete=django.db.models.deletion.DO_NOTHING, related_name='resumes', to='atnp.StudentInDrive'),
        ),
    ]