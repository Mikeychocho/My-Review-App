# Generated by Django 4.1.1 on 2022-09-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_animeinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
