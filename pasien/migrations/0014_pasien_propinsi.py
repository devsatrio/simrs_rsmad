# Generated by Django 4.2 on 2023-04-16 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterWilayah', '0008_kecamatan_alter_kota_options_kelurahan_and_more'),
        ('pasien', '0013_remove_pasien_propinsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasien',
            name='propinsi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='masterWilayah.propinsi'),
        ),
    ]
