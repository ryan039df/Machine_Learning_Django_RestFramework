# Generated by Django 4.2 on 2023-04-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
    ]
