# Generated by Django 4.1.5 on 2023-05-17 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corse', '0006_alter_lectuer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectuer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 17, 22, 20, 19, 414074)),
        ),
    ]
