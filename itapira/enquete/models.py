from django.db import models

# Create your models here.

# vamos criar classes representando as tabelas do banco de dados - cada tabela será uma classe

class Questao(models.Model): #classe Model tem todos os códigos necessários para que o ORM funcione, por isso temos que importar 
    pergunta = models.CharField(max_length=200) # máximo de caracteres
    data = models.DateTimeField(auto_now_add=True) # data vai ser automática

    def __str__(self):
        return f"{self.pergunta} - {self.data}" 

# colunas do bd: pergunta e data
# tipo: CharField para texto e DateTimeField para data e hora
# campo id criado automaticamente

class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE) # se eu apagar a pergunta original, todas as respostas ligadas a ela serão apagadas
    resposta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0) # votação sempre começa com 0 votos

    def __str__(self):
        return self.resposta
