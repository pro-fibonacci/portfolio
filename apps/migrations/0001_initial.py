# Generated by Django 3.0.4 on 2020-03-18 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutme', models.TextField(max_length=50)),
                ('profile', models.ImageField(upload_to='')),
                ('moreaboutme', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client1', models.ImageField(upload_to='')),
                ('client2', models.ImageField(upload_to='')),
                ('client3', models.ImageField(upload_to='')),
                ('client4', models.ImageField(upload_to='')),
                ('client5', models.ImageField(upload_to='')),
                ('client6', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=20)),
                ('profile', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstport', models.ImageField(upload_to='')),
                ('secondport', models.ImageField(upload_to='')),
                ('thirdport', models.ImageField(upload_to='')),
                ('fouthport', models.ImageField(upload_to='')),
                ('fifthport', models.ImageField(upload_to='')),
                ('sixport', models.ImageField(upload_to='')),
                ('sevenport', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ui', models.TextField(max_length=50)),
                ('webdev', models.TextField(max_length=50)),
                ('webdesign', models.TextField(max_length=50)),
                ('brand', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50)),
                ('author', models.TextField(max_length=15)),
            ],
        ),
    ]