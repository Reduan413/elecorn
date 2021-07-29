# Generated by Django 3.2 on 2021-05-04 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('serial_no', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
                ('sub_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.sub_category')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.unit')),
            ],
        ),
    ]
