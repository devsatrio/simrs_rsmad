# Generated by Django 4.2 on 2023-06-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0025_karyawan_kode'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='karyawan/'),
        ),
    ]
