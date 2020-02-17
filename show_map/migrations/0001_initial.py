# Generated by Django 2.2.6 on 2019-10-16 15:21
# _*_ encoding:utf-8 _*_
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('data', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='weights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index1', models.IntegerField()),
                ('index2', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('state', models.IntegerField(default=1)),
            ],
        ),
    ]
