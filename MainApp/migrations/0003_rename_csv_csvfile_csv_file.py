# Generated by Django 4.1.4 on 2022-12-14 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0002_csvfile_timeframe"),
    ]

    operations = [
        migrations.RenameField(
            model_name="csvfile",
            old_name="csv",
            new_name="csv_file",
        ),
    ]
