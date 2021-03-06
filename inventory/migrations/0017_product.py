# Generated by Django 3.2 on 2021-06-03 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('part_no', models.CharField(max_length=50)),
                ('serial_no', models.CharField(max_length=50)),
                ('market_name', models.CharField(max_length=50)),
                ('model_no', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('barcode_type', models.CharField(max_length=100)),
                ('sku_no', models.CharField(max_length=100)),
                ('alert_quantity', models.CharField(max_length=100)),
                ('narration', models.TextField()),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.segment')),
                ('sub_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.sub_category')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.unit')),
            ],
        ),
    ]
