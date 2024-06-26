# Generated by Django 5.0.1 on 2024-04-02 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DbApp', '0004_base1_base2_base3_base4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base5',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('regno', models.IntegerField(primary_key=True, serialize=False)),
                ('carModel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DupEmployee',
            fields=[
            ],
            options={
                'ordering': ['salary'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('DbApp.employee',),
        ),
        migrations.CreateModel(
            name='Base6',
            fields=[
                ('base5_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DbApp.base5')),
                ('empname', models.CharField(max_length=20)),
            ],
            bases=('DbApp.base5',),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('licenseno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('cars', models.ManyToManyField(to='DbApp.car')),
            ],
        ),
    ]
