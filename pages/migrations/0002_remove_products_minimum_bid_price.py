# Generated by Django 3.1.11 on 2021-05-18 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='minimum_bid_price',
        ),
    ]
