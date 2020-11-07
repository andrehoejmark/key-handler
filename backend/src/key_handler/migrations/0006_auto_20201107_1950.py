# Generated by Django 3.1.3 on 2020-11-07 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key_handler', '0005_auto_20201107_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='key',
            old_name='license_key',
            new_name='license',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='license_key',
            new_name='license',
        ),
        migrations.AlterField(
            model_name='session',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 7, 19, 55, 26, 782005)),
        ),
    ]
