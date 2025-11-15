from django.db import models

class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" 
    def __str__(self):
        return self.nome

class Produtos(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    em_estoque = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos" 
    def __str__(self):
        return self.nome

class Clientes(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField(max_length=10)
    email = models.EmailField(max_length=100)
    contato = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes" 
    def __str__(self):
        return self.nome

    
from django.db import models
from django.utils import timezone

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']