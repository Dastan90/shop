# Generated by Django 3.1 on 2021-07-01 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mikey_shirt_shoes_shorts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shoes',
            new_name='Shoe',
        ),
        migrations.RenameModel(
            old_name='Shorts',
            new_name='Short',
        ),
    ]
