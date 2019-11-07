# Generated by Django 2.2.6 on 2019-10-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperatives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coop_name', models.CharField(max_length=200)),
                ('coop_address1', models.CharField(max_length=60)),
                ('coop_address2', models.CharField(max_length=60)),
                ('coop_city', models.CharField(max_length=60)),
                ('coop_province', models.CharField(choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('YT', 'Yukon')], max_length=2)),
                ('coop_country', models.CharField(choices=[('CA', 'Canada'), ('US', 'United States of America')], default='CA', max_length=3)),
            ],
        ),
    ]
