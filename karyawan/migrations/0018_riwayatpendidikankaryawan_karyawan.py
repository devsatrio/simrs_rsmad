# Generated by Django 4.2 on 2023-06-01 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0017_riwayatpendidikankaryawan'),
    ]

    operations = [
        migrations.AddField(
            model_name='riwayatpendidikankaryawan',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='karyawan.karyawan'),
        ),
    ]