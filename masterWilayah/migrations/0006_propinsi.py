# Generated by Django 4.2 on 2023-04-15 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterWilayah', '0005_remove_negara_kode_negara'),
    ]

    operations = [
        migrations.CreateModel(
            name='propinsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('negara', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='masterWilayah.negara')),
            ],
            options={
                'verbose_name': 'Propinsi',
                'verbose_name_plural': 'Propinsi',
            },
        ),
    ]
