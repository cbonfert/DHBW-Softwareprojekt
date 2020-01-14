# Generated by Django 3.0 on 2020-01-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_tourism', '0004_auto_20200113_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='churchentry',
            name='denomination',
            field=models.CharField(choices=[('evangelisch', 'evangelisch'), ('katholisch', 'katholisch'), ('sonstiges', 'sonstiges')], max_length=30, verbose_name='Konfession'),
        ),
        migrations.AlterField(
            model_name='trailentry',
            name='difficulty',
            field=models.CharField(choices=[('leicht', 'leicht'), ('mittel', 'mittel'), ('schwer', 'schwer')], max_length=30, verbose_name='Schwierigkeitsgrad'),
        ),
    ]