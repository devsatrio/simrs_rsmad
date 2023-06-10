# Generated by Django 4.2 on 2023-05-23 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterData', '0007_unit'),
        ('karyawan', '0010_alter_berkaskaryawan_options_berkaskaryawan_karyawan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='masterData.unit'),
        ),
    ]