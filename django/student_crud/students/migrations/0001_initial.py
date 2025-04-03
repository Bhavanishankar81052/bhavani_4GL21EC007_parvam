# Generated by Django 4.2 on 2025-03-25 06:01

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
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('qualification', models.IntegerField()),
                ('experience', models.CharField(max_length=50)),
            ],
        ),
    ]
