# Generated by Django 2.0.7 on 2018-08-05 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180805_2222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminDB',
            new_name='Admin',
        ),
    ]