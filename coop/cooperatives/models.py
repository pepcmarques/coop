from django.db import models


# Create your models here.
class Cooperatives(models.Model):
    PROVINCES_CHOICES = [
        ('AB', 'Alberta'),
        ('BC', 'British Columbia'),
        ('MB', 'Manitoba'),
        ('NB', 'New Brunswick'),
        ('NL', 'Newfoundland and Labrador'),
        ('NS', 'Nova Scotia'),
        ('ON', 'Ontario'),
        ('PE', 'Prince Edward Island'),
        ('QC', 'Quebec'),
        ('SK', 'Saskatchewan'),
        ('NT', 'Northwest Territories'),
        ('NU', 'Nunavut'),
        ('YT', 'Yukon')
    ]

    COUNTRY_CHOICES = [
        ('CA', 'Canada'),
        ('US', 'United States of America'),
    ]

    coop_name = models.CharField(max_length=200,)
    coop_address1 = models.CharField(max_length=60,)
    coop_address2 = models.CharField(max_length=60,)
    coop_city = models.CharField(max_length=60,)
    coop_province = models.CharField(max_length=2, choices=PROVINCES_CHOICES)
    coop_country = models.CharField(max_length=3, choices=COUNTRY_CHOICES, default='CA')
