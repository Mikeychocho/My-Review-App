# Generated by Django 4.1.1 on 2022-09-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_settings_setting'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnimeContent',
        ),
        migrations.AddField(
            model_name='animeinfo',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='animeinfo',
            name='image',
            field=models.FileField(max_length=200, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='animeinfo',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='animeinfo',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='animeinfo',
            name='status',
            field=models.CharField(choices=[('Still Airing', 'Still Airing'), ('Completed', 'Completed')], max_length=20, null=True),
        ),
    ]
