# Generated by Django 2.0 on 2019-01-04 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DOJ',
            field=models.DateField(default=datetime.datetime(2019, 1, 4, 17, 17, 41, 191515, tzinfo=utc)),
        ),
    ]
