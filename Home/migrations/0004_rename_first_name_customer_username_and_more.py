# Generated by Django 5.0.1 on 2024-04-26 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
