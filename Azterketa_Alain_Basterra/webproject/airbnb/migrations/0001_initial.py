# Generated by Django 4.2.6 on 2023-10-17 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pertsona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=100)),
                ('emaila', models.CharField(max_length=100)),
                ('nan', models.CharField(max_length=9)),
                ('sortu_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etxea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=100)),
                ('herria', models.CharField(max_length=100)),
                ('pertsona_kopurua', models.IntegerField()),
                ('sortu_data', models.DateTimeField(auto_now_add=True)),
                ('alokatu_hasi', models.DateTimeField()),
                ('alokatu_bukatu', models.DateTimeField()),
                ('egoera', models.CharField(max_length=100)),
                ('pertsona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airbnb.pertsona')),
            ],
        ),
    ]