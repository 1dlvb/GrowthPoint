# Generated by Django 3.2 on 2021-05-04 12:15

from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20210503_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preview_text',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='Федеральная сеть центров образования цифрового, естественнонаучного, технического и гуманитарного профилей, организованная в рамках проекта "Современная школа"', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=web.models.LimitedImageField(blank=True, upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.post'),
        ),
    ]
