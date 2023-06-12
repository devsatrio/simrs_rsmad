# Generated by Django 4.2 on 2023-06-11 12:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
import pasien.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterWilayah', '0001_initial'),
        ('masterData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pasien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_rkm_medis', models.CharField(blank=True, default=pasien.models.create_new_ref_number, editable=False, max_length=10, unique=True)),
                ('nama', models.CharField(max_length=200)),
                ('no_ktp', models.CharField(max_length=50, null=True)),
                ('tgl_lahir', models.DateField()),
                ('tgl_daftar', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('no_telfon', models.CharField(max_length=50, null=True)),
                ('nip', models.CharField(blank=True, max_length=50, null=True)),
                ('agama', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.agama')),
                ('golongan_darah', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.golongandarah')),
                ('jenis_kelamin', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='masterData.jeniskelamin')),
                ('jenis_pekerjaan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.jenispekerjaan')),
                ('kecamatan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.kecamatan')),
                ('kelurahan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.kelurahan')),
                ('kota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.kota')),
                ('negara', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.negara')),
                ('propinsi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.propinsi')),
                ('status_nikah', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.statusnikah')),
                ('strata_pendidikan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.stratapendidikan')),
            ],
            options={
                'verbose_name': 'Data Pasien',
                'verbose_name_plural': 'Data Pasien',
            },
        ),
    ]
