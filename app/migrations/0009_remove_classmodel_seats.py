# Generated by Django 3.1.7 on 2021-04-15 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210415_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classmodel',
            name='seats',
        ),
    ]
