from django.db import models
from django.urls import reverse
# from django.core.validators import RegexValidator
# Create your models here.

class Anagrafica(models.Model):
    codottico = models.AutoField(primary_key = True) #come poterlo vedere/modificare
    nome = models.CharField(max_length = 50)
    indirizzo = models.CharField(max_length = 50)
    citta = models.CharField(max_length = 50)
    provincia = models.CharField(max_length = 2)
    cap = models.CharField(max_length = 5)
    nome2 = models.CharField(max_length = 50, default = "-")
    indirizzo2 = models.CharField(max_length = 50, default = "-")
    citta2 = models.CharField(max_length = 50, default = "-")
    provincia2 = models.CharField(max_length = 2, default = "-")
    cap2 = models.CharField(max_length = 5, default = "00000")
    telefono = models.CharField(max_length = 10)
    cellurare = models.CharField(max_length = 10, default = "-")
    codice_fiscale = models.CharField(max_length = 16)
    p_iva = models.CharField(max_length = 11)
    sconto_gen = models.CharField(max_length = 2, default = "0")
    cod_pag = models.CharField(max_length = 10)
    pagamento = models.CharField(max_length = 50)
    banca = models.CharField(max_length = 50)
    iban = models.CharField(max_length = 27)
    abi = models.CharField(max_length = 5, default = "00000")
    cab = models.CharField(max_length = 5, default = "00000")
    fa = models.CharField(max_length = 50, default = "-")
    spedizione = models.CharField(max_length = 50)
    pagcorr = models.CharField(max_length = 50)
    note = models.CharField(max_length = 50, default = "-")
    data_registrazione = models.DateField(auto_now_add=True)
    codcpa = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, default = "mail_di_prova@gmail.it")
    pec = models.EmailField(max_length = 50, default = "mail_di_prova@pec.it")
    applicatore =  models.CharField(max_length = 50)


    # capire perchè non funziona
    def get_absolute_url(self):
        return reverse("anagrafica:anagrafica-detail", kwargs={"id":self.codottico})
    