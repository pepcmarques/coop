# Generated by Django 2.2.6 on 2019-10-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191029_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False, verbose_name='staff'),
        ),
    ]
