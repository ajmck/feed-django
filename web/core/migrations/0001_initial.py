# Generated by Django 2.0 on 2018-08-21 06:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time Posted')),
                ('post_location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'ordering': ['pub_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time Posted')),
                ('post_location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'ordering': ['-pub_date'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_fk', to='core.Post'),
        ),
    ]
