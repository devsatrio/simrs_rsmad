# Generated by Django 4.2 on 2023-11-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterData', '0006_penyakit_prosedur'),
    ]

    operations = [
        migrations.AddField(
            model_name='perawatan_rawat_jalan',
            name='total_biaya',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
