# Generated by Django 4.1.2 on 2023-03-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_alter_item_sub_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Sub_image',
            field=models.ImageField(upload_to='subject_img'),
        ),
    ]
