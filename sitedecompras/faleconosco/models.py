from django.db import models

class Contato(models.Model): 
    nome = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 60)
    mensagem = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.nome, self.email)

