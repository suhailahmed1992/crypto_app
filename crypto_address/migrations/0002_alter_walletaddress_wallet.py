# Generated by Django 3.2.18 on 2023-04-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletaddress',
            name='wallet',
            field=models.CharField(choices=[('ETH', 'Ethereum'), ('BTC', 'Bitcoin')], max_length=25),
        ),
    ]
