# Generated by Django 4.1.5 on 2023-04-17 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corse', '0004_alter_lectuer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectuer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 6, 47, 25, 531395)),
        ),
    ]
