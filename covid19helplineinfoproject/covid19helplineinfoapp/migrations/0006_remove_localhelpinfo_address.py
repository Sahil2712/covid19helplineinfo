# Generated by Django 3.0.4 on 2020-03-22 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid19helplineinfoapp', '0005_auto_20200322_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localhelpinfo',
            name='address',
        ),
    ]
