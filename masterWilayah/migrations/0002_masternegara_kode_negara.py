# Generated by Django 4.2 on 2023-04-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterWilayah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masternegara',
            name='kode_negara',
            field=models.IntegerField(null=True),
        ),
    ]
