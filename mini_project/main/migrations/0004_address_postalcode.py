# Generated by Django 4.2.6 on 2023-11-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='postalcode',
            field=models.IntegerField(default=1),
        ),
    ]
