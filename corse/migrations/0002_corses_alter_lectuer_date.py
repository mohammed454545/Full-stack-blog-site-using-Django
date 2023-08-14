# Generated by Django 4.1.5 on 2023-03-13 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('discribtion', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='lectuer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 13, 11, 51, 29, 618177)),
        ),
    ]
