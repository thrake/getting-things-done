# Generated by Django 2.2 on 2019-05-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0009_auto_20190506_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capture',
            name='notes',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
