# Generated by Django 4.2 on 2023-11-26 04:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0002_remove_registrasi_jam_registrasi_and_more'),
        ('karyawan', '0007_alter_absensikaryawan_jam_masuk_karyawan_and_more'),
        ('masterData', '0007_perawatan_rawat_jalan_total_biaya'),
        ('rekamMedis', '0002_diagnosa_created_at_diagnosa_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tindakan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Primary', 'Primary'), ('Sekunder', 'Sekunder')], default='Primary', max_length=50)),
                ('tindakan_dokter', models.TextField(blank=True, max_length=300, null=True)),
                ('status_periksa', models.CharField(choices=[('RALAN', 'RALAN'), ('RANAP', 'RANAP')], default='RALAN', max_length=50)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='created_by_tindakan', to='karyawan.karyawan')),
                ('dokter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='dokter_pemberi_tindakan', to='karyawan.karyawan')),
                ('no_rawat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='frontoffice.registrasi')),
                ('tindakan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.prosedur')),
            ],
            options={
                'verbose_name': 'Tindakan (ICD 9)',
                'verbose_name_plural': 'Tindakan (ICD 9)',
            },
        ),
    ]
