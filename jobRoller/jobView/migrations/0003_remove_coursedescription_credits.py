# Generated by Django 2.0.7 on 2019-04-23 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobView', '0002_auto_20190423_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedescription',
            name='credits',
        ),
    ]
