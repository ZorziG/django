# Generated by Django 4.0.5 on 2022-07-03 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0005_alter_anagrafica_email_alter_anagrafica_pec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='cap',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='cap2',
            field=models.IntegerField(default='00000', max_length=5),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='p_iva',
            field=models.IntegerField(default='00000000000', max_length=11),
        ),
    ]