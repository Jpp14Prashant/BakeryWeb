# Generated by Django 4.2.2 on 2023-07-11 07:23

import bakery_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_app', '0003_banner_delete_accessorybanner_delete_cakebanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_photo',
            field=models.ImageField(upload_to='banner_images/', validators=[bakery_app.models.validate_banner_image]),
        ),
    ]
