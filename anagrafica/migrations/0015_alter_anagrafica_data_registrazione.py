# Generated by Django 4.0.5 on 2022-07-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0014_alter_anagrafica_abi_alter_anagrafica_cab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='data_registrazione',
            field=models.DateField(auto_now_add=True),
        ),
    ]