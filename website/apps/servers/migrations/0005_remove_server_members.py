# Generated by Django 2.1.5 on 2019-04-04 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_auto_20190404_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='members',
        ),
    ]
