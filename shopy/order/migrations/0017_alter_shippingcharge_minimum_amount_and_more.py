# Generated by Django 5.0.6 on 2024-07-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_shippingcharge_minimum_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingcharge',
            name='minimum_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shippingcharge',
            name='shipping_charge',
            field=models.IntegerField(default=0),
        ),
    ]