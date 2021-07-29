# Generated by Django 3.2 on 2021-06-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('license_no', models.CharField(max_length=50)),
            ],
        ),
    ]
