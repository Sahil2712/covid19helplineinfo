# Generated by Django 2.2 on 2020-03-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19helplineinfoapp', '0010_dashboard_important_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
    ]
