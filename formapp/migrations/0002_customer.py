# Generated by Django 4.1.4 on 2022-12-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('mob', models.PositiveBigIntegerField()),
                ('English', models.BooleanField()),
                ('Kannada', models.BooleanField()),
                ('Hindi', models.BooleanField()),
                ('Telugu', models.BooleanField()),
                ('Tamil', models.BooleanField()),
            ],
        ),
    ]