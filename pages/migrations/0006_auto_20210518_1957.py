# Generated by Django 3.1.11 on 2021-05-18 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_products_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('date_posted',)},
        ),
        migrations.AlterIndexTogether(
            name='products',
            index_together={('id', 'slug')},
        ),
    ]
