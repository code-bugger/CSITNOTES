# Generated by Django 4.1.2 on 2023-03-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_rename_items_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Sub_image',
            field=models.ImageField(upload_to='subject_img/'),
        ),
    ]
