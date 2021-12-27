# Generated by Django 3.2.7 on 2021-12-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.TextField()),
                ('year', models.TextField()),
                ('wins', models.TextField()),
                ('losses', models.TextField()),
                ('points', models.TextField()),
                ('goals_scored', models.TextField()),
                ('goals_allowed', models.TextField()),
                ('goals_per90', models.TextField()),
                ('assists_per90', models.TextField()),
                ('clean_sheets', models.TextField()),
                ('table_finish', models.TextField()),
            ],
        ),
    ]
