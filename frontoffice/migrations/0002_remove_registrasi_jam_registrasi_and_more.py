# Generated by Django 4.2 on 2023-11-25 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrasi',
            name='jam_registrasi',
        ),
        migrations.AlterField(
            model_name='registrasi',
            name='tgl_registrasi',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
