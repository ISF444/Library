# Generated by Django 4.2.1 on 2023-05-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisNewReaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname_of_readers', models.CharField(max_length=100)),
                ('name_of_readers', models.CharField(max_length=100)),
                ('middle_name_of_readers', models.CharField(blank=True, max_length=100)),
                ('passport_id', models.CharField(blank=True, max_length=10, unique=True)),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('residential_address', models.CharField(blank=True, max_length=100)),
                ('data_of_birth', models.DateField()),
            ],
        ),
    ]
