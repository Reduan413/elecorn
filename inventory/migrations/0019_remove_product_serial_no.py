# Generated by Django 3.2 on 2021-06-09 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_rename_segment_product_segment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='serial_no',
        ),
    ]