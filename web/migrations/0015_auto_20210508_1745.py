# Generated by Django 3.2 on 2021-05-08 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20210508_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='postadditionaltext',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.post'),
        ),
        migrations.AddField(
            model_name='postadditionaltext',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
