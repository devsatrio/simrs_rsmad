# Generated by Django 4.2 on 2023-11-20 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontoffice', '0001_initial'),
        ('masterData', '0006_penyakit_prosedur'),
    ]

    operations = [
        migrations.CreateModel(
            name='kategori_perawatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Kategori Perawatan',
                'verbose_name_plural': 'Kategori Perawatan',
            },
        ),
        migrations.CreateModel(
            name='perawatan_rawat_jalan_pasien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perawatan', models.CharField(max_length=50)),
                ('biaya_material', models.IntegerField(blank=True, null=True)),
                ('biaya_bhp', models.IntegerField(blank=True, null=True)),
                ('biaya_dokter', models.IntegerField(blank=True, null=True)),
                ('biaya_perawat', models.IntegerField(blank=True, null=True)),
                ('biaya_kso', models.IntegerField(blank=True, null=True)),
                ('biaya_manajemen', models.IntegerField(blank=True, null=True)),
                ('biaya_rawat', models.IntegerField(blank=True, null=True)),
                ('kategori', models.ForeignKey(blank=True, help_text='Kategori perawatan dokter / perawat', null=True, on_delete=django.db.models.deletion.RESTRICT, to='pelayanan_medis.kategori_perawatan')),
                ('no_rawat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='frontoffice.registrasi')),
                ('perawatan_rawat_jalan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.perawatan_rawat_jalan')),
            ],
            options={
                'verbose_name': 'Perawatan Rawat Jalan Pasien',
                'verbose_name_plural': 'Perawatan Rawat Jalan Pasien',
            },
        ),
    ]