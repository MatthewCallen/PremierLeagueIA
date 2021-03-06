# Generated by Django 3.2.7 on 2021-12-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StatsTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='draws',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stats',
            name='assists_per90',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='clean_sheets',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='goals_allowed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='goals_per90',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='goals_scored',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='losses',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='table_finish',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='wins',
            field=models.IntegerField(),
        ),
    ]
