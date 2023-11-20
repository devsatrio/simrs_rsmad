# Generated by Django 4.2 on 2023-11-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterData', '0005_perawatan_rawat_jalan_biaya_bhp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penyakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=30, unique=True)),
                ('nama', models.CharField(max_length=50)),
                ('ciri_ciri', models.TextField(blank=True, max_length=300, null=True)),
                ('keterangan', models.TextField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(choices=[('Tidak Menular', 'Tidak Menular'), ('Menular', 'Menular')], default='Tidak Menular', max_length=50)),
            ],
            options={
                'verbose_name': 'Penyakit',
                'verbose_name_plural': 'Penyakit',
            },
        ),
        migrations.CreateModel(
            name='Prosedur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=30, unique=True)),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Prosedur',
                'verbose_name_plural': 'Prosedur',
            },
        ),
    ]