# Generated by Django 4.2.6 on 2023-12-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_address_postalcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postalcode',
            field=models.IntegerField(default=1),
        ),
    ]
