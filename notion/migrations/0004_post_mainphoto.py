# Generated by Django 3.1.3 on 2020-11-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notion', '0003_auto_20201121_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
