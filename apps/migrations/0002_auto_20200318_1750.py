# Generated by Django 3.0.4 on 2020-03-18 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Ui',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='services',
            name='brand',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='services',
            name='webdesign',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='services',
            name='webdev',
            field=models.TextField(max_length=5000),
        ),
    ]
