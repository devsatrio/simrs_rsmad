# Generated by Django 4.2.2 on 2023-06-19 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kecamatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Kecamatan',
                'verbose_name_plural': 'Kecamatan',
            },
        ),
        migrations.CreateModel(
            name='negara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=80)),
                ('nicename', models.CharField(max_length=80)),
                ('iso3', models.CharField(max_length=10)),
                ('numcode', models.IntegerField()),
                ('phonecode', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Negara',
                'verbose_name_plural': 'Negara',
            },
        ),
        migrations.CreateModel(
            name='propinsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('negara', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.negara')),
            ],
            options={
                'verbose_name': 'Propinsi',
                'verbose_name_plural': 'Propinsi',
            },
        ),
        migrations.CreateModel(
            name='kota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('propinsi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.propinsi')),
            ],
            options={
                'verbose_name': 'Kota',
                'verbose_name_plural': 'Kota',
            },
        ),
        migrations.CreateModel(
            name='kelurahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('kecamatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.kecamatan')),
            ],
            options={
                'verbose_name': 'Kelurahan',
                'verbose_name_plural': 'Kelurahan',
            },
        ),
        migrations.AddField(
            model_name='kecamatan',
            name='kota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterWilayah.kota'),
        ),
    ]
