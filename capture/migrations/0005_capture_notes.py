# Generated by Django 2.2 on 2019-05-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0004_auto_20190501_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='capture',
            name='notes',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
