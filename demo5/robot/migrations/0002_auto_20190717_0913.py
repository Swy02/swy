# Generated by Django 2.2.3 on 2019-07-17 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Titles',
        ),
    ]