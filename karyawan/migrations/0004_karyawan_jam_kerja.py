# Generated by Django 4.1 on 2023-07-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0003_alter_jamkerja_keterangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='jam_kerja',
            field=models.ManyToManyField(blank=True, to='karyawan.jamkerja'),
        ),
    ]
