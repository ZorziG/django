# Generated by Django 4.0.5 on 2022-07-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0012_alter_anagrafica_cap2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='cap2',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]
