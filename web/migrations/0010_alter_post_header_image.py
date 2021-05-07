# Generated by Django 3.2 on 2021-05-07 14:17

from django.db import migrations
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20210504_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=web.models.LimitedImageField(default='images/empty_image.jpg', help_text='Header image should be 400x400 in size.', upload_to='images/', verbose_name='Header Image'),
        ),
    ]
