# Generated by Django 4.1 on 2023-07-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0006_absensikaryawan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absensikaryawan',
            name='jam_masuk_karyawan',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='absensikaryawan',
            name='jam_pulang_karyawan',
            field=models.TimeField(blank=True, null=True),
        ),
    ]