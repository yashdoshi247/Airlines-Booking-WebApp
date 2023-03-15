# Generated by Django 4.1 on 2023-03-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=65)),
                ('destination', models.CharField(max_length=65)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
