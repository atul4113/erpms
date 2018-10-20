# Generated by Django 2.0.7 on 2018-08-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180804_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDB',
            fields=[
                ('ausr', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('aemail', models.EmailField(default='admin@test.com', max_length=254)),
                ('apw', models.CharField(max_length=20)),
                ('e_name', models.CharField(max_length=25)),
                ('e_email', models.EmailField(max_length=254)),
                ('e_mobile', models.IntegerField(default=9876543210)),
                ('e_exams', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]