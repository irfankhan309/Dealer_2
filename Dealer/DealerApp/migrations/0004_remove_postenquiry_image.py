# Generated by Django 2.1.5 on 2019-03-22 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DealerApp', '0003_auto_20190322_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postenquiry',
            name='Image',
        ),
    ]
