# Generated by Django 3.1.11 on 2021-05-19 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]