# Generated by Django 3.2 on 2021-04-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20210427_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]
