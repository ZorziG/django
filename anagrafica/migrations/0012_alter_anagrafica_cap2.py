# Generated by Django 4.0.5 on 2022-07-03 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0011_alter_anagrafica_abi_alter_anagrafica_cab_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='cap2',
            field=models.CharField(default=0, max_length=5, validators=[django.core.validators.RegexValidator('^\\d*5$')]),
        ),
    ]
