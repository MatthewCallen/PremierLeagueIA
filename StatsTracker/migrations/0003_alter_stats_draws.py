# Generated by Django 3.2.7 on 2021-12-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StatsTracker', '0002_auto_20211223_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='draws',
            field=models.IntegerField(default=0),
        ),
    ]