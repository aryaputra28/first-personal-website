# Generated by Django 3.1.1 on 2020-10-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story6', '0003_auto_20201020_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='kegiatansaya',
            name='Deskripsi',
            field=models.TextField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]