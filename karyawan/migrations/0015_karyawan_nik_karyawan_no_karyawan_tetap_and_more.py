# Generated by Django 4.2 on 2023-05-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0014_alter_berkaskaryawan_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='nik',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='no_karyawan_tetap',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='no_sip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='no_str',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='no_telfon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='tempat_lahir',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='tgl_berlaku_sip',
            field=models.DateField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='tgl_berlaku_str',
            field=models.DateField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='tgl_lahir',
            field=models.DateField(blank=True, max_length=30, null=True),
        ),
    ]