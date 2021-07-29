# Generated by Django 3.2 on 2021-06-20 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_cost_center_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='company',
            new_name='company_id',
        ),
        migrations.RemoveField(
            model_name='cost_center',
            name='company',
        ),
        migrations.AddField(
            model_name='cost_center',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
            preserve_default=False,
        ),
    ]