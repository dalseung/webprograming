# Generated by Django 3.1.3 on 2020-11-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notion', '0010_remove_post_pw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
