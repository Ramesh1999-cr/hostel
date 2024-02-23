# Generated by Django 5.0.2 on 2024-02-14 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=149, null=True)),
                ('working_timing', models.TimeField()),
                ('address', models.TextField(max_length=250, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='person_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=70, null=True)),
                ('last_name', models.CharField(blank=True, max_length=140, null=True)),
                ('father_name', models.CharField(blank=True, max_length=170, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('telephone_name', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('parement_address', models.TextField(blank=True, max_length=240, null=True)),
                ('state', models.CharField(blank=True, max_length=189, null=True)),
                ('country', models.CharField(blank=True, max_length=184, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='floors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_number', models.IntegerField(blank=True)),
                ('room_number', models.IntegerField(blank=True)),
                ('room_sharing', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple')], max_length=10)),
                ('amount_paid', models.BooleanField(blank=True, default='')),
                ('joining_data', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floors.user')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
