# Generated by Django 5.0.1 on 2024-04-26 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_rename_first_name_customer_username_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Userdata',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
