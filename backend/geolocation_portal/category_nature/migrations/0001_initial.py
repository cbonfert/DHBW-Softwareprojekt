# Generated by Django 3.0 on 2019-12-23 12:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geomodels', '0009_auto_20191223_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewpointEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=15, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Aussichtspunkt',
                'verbose_name_plural': 'Aussichtspunkte',
            },
        ),
    ]
