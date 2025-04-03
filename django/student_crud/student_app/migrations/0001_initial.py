# Generated by Django 4.2 on 2025-03-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('usn', models.CharField(max_length=20, unique=True)),
                ('branch', models.CharField(max_length=50)),
                ('sem', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
