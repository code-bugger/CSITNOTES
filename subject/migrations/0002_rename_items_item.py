# Generated by Django 4.1.2 on 2023-03-26 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='item',
        ),
    ]