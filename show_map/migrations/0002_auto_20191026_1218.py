# Generated by Django 2.2.6 on 2019-10-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address_info',
            name='data',
            field=models.CharField(max_length=20),
        ),
    ]