# Generated by Django 2.1.5 on 2019-03-22 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DealerApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BikePurchase',
        ),
        migrations.DeleteModel(
            name='BikeSale',
        ),
    ]
