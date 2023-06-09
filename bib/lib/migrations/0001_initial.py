# Generated by Django 4.2.1 on 2023-05-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRegis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100)),
                ('name_orig', models.CharField(blank=True, max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=1000)),
                ('quant_copies', models.IntegerField(max_length=100)),
                ('all_authors', models.CharField(max_length=100)),
                ('foto_covers', models.ImageField(upload_to=None)),
                ('foto_authors', models.ImageField(blank=True, upload_to=None)),
                ('price_per_day', models.IntegerField(max_length=1000)),
                ('year_of_publish', models.DateField(blank=True)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('numbers_of_pages', models.IntegerField(blank=True, max_length=10000)),
            ],
        ),
    ]
