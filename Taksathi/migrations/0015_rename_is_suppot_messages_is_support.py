# Generated by Django 4.0.4 on 2022-05-12 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Taksathi', '0014_messages_is_suppot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='is_suppot',
            new_name='is_support',
        ),
    ]
