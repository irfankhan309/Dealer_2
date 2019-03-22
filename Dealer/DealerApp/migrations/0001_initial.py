# Generated by Django 2.1.5 on 2019-03-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikePurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=45)),
                ('Description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='BikeSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=45)),
                ('Description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PostEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Vehicle', models.CharField(max_length=40)),
                ('BIKE_Model', models.CharField(max_length=35)),
                ('Color', models.CharField(max_length=35)),
                ('Contact_Number', models.CharField(max_length=15)),
            ],
        ),
    ]
