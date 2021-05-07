# Generated by Django 3.2 on 2021-05-03 16:37

from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_text',
            field=models.CharField(default='федеральная сеть центров образования цифрового, естественнонаучного, технического и гуманитарного профилей, организованная в рамках проекта "Современная школа"', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=web.models.LimitedImageField(default='images/empty_image.jpg', help_text='Header image should be 400x300 in size.', upload_to='images/', verbose_name='Header Image'),
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', web.models.LimitedImageField(upload_to='images/', verbose_name='Image')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.post')),
            ],
        ),
    ]