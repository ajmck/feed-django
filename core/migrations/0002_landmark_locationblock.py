# Generated by Django 2.0 on 2018-08-21 06:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('moderation', models.CharField(choices=[('US', 'User Submitted'), ('AP', 'Approved'), ('FL', 'Flagged')], default='US', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='LocationBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]