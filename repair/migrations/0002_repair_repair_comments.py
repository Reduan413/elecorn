# Generated by Django 3.2.4 on 2021-06-28 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(max_length=255)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repair_item', to='repair.repair_request')),
            ],
        ),
        migrations.CreateModel(
            name='Repair_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repair_item', to='repair.repair')),
            ],
        ),
    ]
