# Generated by Django 4.1.1 on 2022-09-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_animecontents_animeinfo_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='darkmode',
            field=models.CharField(choices=[('darkmode', 'darkmode'), ('lightmode', 'lightmode')], max_length=200, null=True),
        ),
    ]
