from django.db import models


class BookRegis(models.Model):
    name_ru = models.CharField(max_length=100, blank=False)
    name_orig = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(max_length=1000, blank=False)
    quant_copies = models.IntegerField(max_length=100, blank=False)
    all_authors = models.CharField(max_length=100, blank=False)
    foto_covers = models.ImageField(upload_to=None, blank=False)
    foto_authors = models.ImageField(upload_to=None, blank=True)
    price_per_day = models.IntegerField(max_length=1000, blank=False)
    year_of_publish = models.DateField(blank=True)
    registration_date = models.DateField(auto_now_add=True, blank=True)
    numbers_of_pages = models.IntegerField(max_length=10000, blank=True)

    def __str__(self):
        return self.name_ru


class RegisNewReaders(models.Model):
    surname_of_readers = models.CharField(max_length=100, blank=False)
    name_of_readers = models.CharField(max_length=100, blank=False)
    middle_name_of_readers = models.CharField(max_length=100, blank=True)
    passport_id = models.CharField(max_length=10, unique=True, blank=True)
    e_mail = models.EmailField(max_length=254, unique=True, blank=False)
    residential_address = models.CharField(max_length=100, blank=True)
    data_of_birth = models.DateField(blank=False)

    def __str__(self):
        return self.surname_of_readers



