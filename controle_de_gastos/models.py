from django.db import models

class Categoria(models.Model):
    TIPO_DESPESA = 'despesa'
    TIPO_RECEITA = 'receita'
    TIPO_CHOICES = [
        (TIPO_DESPESA, 'Despesa'),
        (TIPO_RECEITA, 'Receita'),
    ]


    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.title

class Movimentacao(models.Model)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = CharField(max_length=200)
    data = DateField()
    categoria = ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
    usuario = ForeignKey('auth.User', on_delete=models.CASCADE), null=False.+