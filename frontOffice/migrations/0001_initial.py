# Generated by Django 4.2 on 2023-04-20 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterData', '0003_bangsal_alter_poliklinik_options'),
        ('pasien', '0001_initial'),
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrasiPasien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_rawat', models.CharField(max_length=50)),
                ('no_registrasi', models.CharField(max_length=50)),
                ('tgl_registrasi', models.DateField(auto_now=True)),
                ('jam_registrasi', models.TimeField(auto_now=True)),
                ('penanggung_jawab_pasien', models.CharField(max_length=50)),
                ('status_periksa', models.CharField(choices=[('RALAN', 'RALAN'), ('RANAP', 'RANAP')], default='RALAN', max_length=50)),
                ('asuransi_pasien', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterData.asuransi')),
                ('dokter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='karyawan.karyawan')),
                ('pasien', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pasien.pasien', to_field='no_rkm_medis')),
                ('poliklinik', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterData.poliklinik')),
            ],
            options={
                'verbose_name': 'Registrasi',
                'verbose_name_plural': 'Registrasi',
            },
        ),
    ]
