# Generated by Django 2.0.7 on 2018-08-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180805_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindb',
            name='e_email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
        ),
    ]
