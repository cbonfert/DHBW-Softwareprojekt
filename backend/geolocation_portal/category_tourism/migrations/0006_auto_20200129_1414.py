# Generated by Django 3.0 on 2020-01-29 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_tourism', '0005_auto_20200114_0746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addressaccommodationentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='addresschurchentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='addressmonumententry',
            options={'verbose_name_plural': 'Adresse'},
        ),
    ]
