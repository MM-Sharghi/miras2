# Generated by Django 4.0.4 on 2022-05-11 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Derakhti', '0016_derakhtiproducts_vocher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainuser',
            name='identifierـcode',
        ),
        migrations.RemoveField(
            model_name='mainuser',
            name='places',
        ),
    ]
