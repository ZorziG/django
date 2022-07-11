# Generated by Django 4.0.5 on 2022-07-02 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anagrafica',
            fields=[
                ('codottico', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('indirizzo', models.CharField(max_length=50)),
                ('citta', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=2)),
                ('cap', models.CharField(max_length=5)),
                ('nome2', models.CharField(max_length=50)),
                ('indirizzo2', models.CharField(max_length=50)),
                ('citta2', models.CharField(max_length=50)),
                ('provincia2', models.CharField(max_length=2)),
                ('cap2', models.CharField(max_length=5)),
                ('telefono', models.CharField(max_length=10)),
                ('cellurare', models.CharField(max_length=10)),
                ('codice_fiscale', models.CharField(max_length=16)),
                ('p_iva', models.CharField(max_length=11)),
                ('sconto_gen', models.CharField(max_length=2)),
                ('cod_pag', models.CharField(max_length=10)),
                ('pagamento', models.CharField(max_length=50)),
                ('banca', models.CharField(max_length=50)),
                ('iban', models.CharField(max_length=27)),
                ('abi', models.CharField(max_length=5)),
                ('cab', models.CharField(max_length=5)),
                ('fa', models.CharField(max_length=50)),
                ('spedizione', models.CharField(max_length=50)),
                ('pagcorr', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=50)),
                ('data_registrazione', models.DateTimeField(default=datetime.date.today)),
                ('codcpa', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('pec', models.EmailField(max_length=50)),
                ('applicatore', models.CharField(max_length=50)),
            ],
        ),
    ]
