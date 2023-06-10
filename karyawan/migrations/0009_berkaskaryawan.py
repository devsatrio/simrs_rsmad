# Generated by Django 4.2 on 2023-05-23 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0008_alter_kategoriberkaskaryawan_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BerkasKaryawan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_berkas', models.CharField(max_length=200)),
                ('berkas', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='karyawan.kategoriberkaskaryawan')),
            ],
            options={
                'verbose_name': 'Kategori Berkas',
                'verbose_name_plural': 'Kategori Berkas',
            },
        ),
    ]