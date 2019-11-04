# Generated by Django 2.2.5 on 2019-10-14 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atnp', '0025_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='category',
            field=models.EmailField(db_column='category', default='NONE', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='jobOpening',
            field=models.ForeignKey(db_column='jobOpening', on_delete=django.db.models.deletion.CASCADE, to='atnp.JobOpening'),
        ),
        migrations.AlterField(
            model_name='application',
            name='round',
            field=models.ForeignKey(blank=True, db_column='round', null=True, on_delete=django.db.models.deletion.CASCADE, to='atnp.Round'),
        ),
        migrations.AlterField(
            model_name='companyindrive',
            name='drive',
            field=models.ForeignKey(db_column='drive', on_delete=django.db.models.deletion.CASCADE, to='atnp.Drive'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='companyInDrive',
            field=models.ForeignKey(db_column='companyInDrive', on_delete=django.db.models.deletion.CASCADE, related_name='jobOpenings', to='atnp.CompanyInDrive'),
        ),
        migrations.AlterField(
            model_name='resumeopening',
            name='studentInDrive',
            field=models.ForeignKey(db_column='studentInDrive', on_delete=django.db.models.deletion.CASCADE, related_name='resumeOpenings', to='atnp.StudentInDrive'),
        ),
        migrations.AlterField(
            model_name='round',
            name='jobOpening',
            field=models.ForeignKey(db_column='jobOpening', on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='atnp.JobOpening'),
        ),
        migrations.AlterField(
            model_name='studentindrive',
            name='drive',
            field=models.ForeignKey(db_column='drive', on_delete=django.db.models.deletion.CASCADE, to='atnp.Drive'),
        ),
    ]
