# Generated by Django 4.2 on 2023-06-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0022_alter_karirkaryawan_berkas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karirkaryawan',
            name='tahun_berhenti_menjabat',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='karirkaryawan',
            name='tahun_menjabat',
            field=models.IntegerField(max_length=5),
        ),
    ]