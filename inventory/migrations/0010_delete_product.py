# Generated by Django 3.2 on 2021-05-04 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_product_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
