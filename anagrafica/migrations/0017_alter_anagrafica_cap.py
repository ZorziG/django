# Generated by Django 4.0.5 on 2022-07-03 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0016_alter_anagrafica_cap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='cap',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^\\d*5$')]),
        ),
    ]
