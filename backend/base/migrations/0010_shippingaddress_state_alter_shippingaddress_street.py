# Generated by Django 4.2.4 on 2023-09-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_dish_orderitem_dishid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='street',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
