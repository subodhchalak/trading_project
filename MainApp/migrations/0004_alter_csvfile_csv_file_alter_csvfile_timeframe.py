# Generated by Django 4.1.4 on 2022-12-14 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0003_rename_csv_csvfile_csv_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="csvfile",
            name="csv_file",
            field=models.FileField(
                help_text="Please upload only .csv file",
                upload_to="csvfiles/",
                validators=[django.core.validators.FileExtensionValidator(["csv"])],
                verbose_name="CSV File",
            ),
        ),
        migrations.AlterField(
            model_name="csvfile",
            name="timeframe",
            field=models.IntegerField(
                blank=True,
                help_text="Please enter the timefram in minutes and should be grater than 1 minute",
                null=True,
                verbose_name="Timeframe",
            ),
        ),
    ]
