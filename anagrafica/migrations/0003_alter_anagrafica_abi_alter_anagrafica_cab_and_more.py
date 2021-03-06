# Generated by Django 4.0.5 on 2022-07-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0002_alter_anagrafica_data_registrazione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='abi',
            field=models.CharField(default=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='cab',
            field=models.CharField(default=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='cap2',
            field=models.CharField(default=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='cellurare',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='citta2',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='fa',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='indirizzo2',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='nome2',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='note',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='pec',
            field=models.EmailField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='provincia2',
            field=models.CharField(default=False, max_length=2),
        ),
    ]
