# Generated by Django 4.2 on 2023-04-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JenisPekerjaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Jenis Pekerjaan',
                'verbose_name_plural': 'Jenis Pekerjaan',
            },
        ),
        migrations.CreateModel(
            name='StrataPendidikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Strata Pendidikan',
                'verbose_name_plural': 'Strata Pendidikan',
            },
        ),
    ]
