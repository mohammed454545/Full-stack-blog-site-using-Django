# Generated by Django 4.1.5 on 2023-05-18 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corse', '0009_lectuer_des_alter_lectuer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectuer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 12, 55, 35, 681985)),
        ),
    ]