# Generated by Django 2.2 on 2019-05-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0002_auto_20190429_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='capture',
            name='group',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
