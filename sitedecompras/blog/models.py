# -*- coding:utf8 -*-
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Título") 
    post = models.TextField() 
    created_at = models.DateTimeField(auto_now_add = True) 
    last_modified = models.DateTimeField(auto_now = True) 
    categories = models.ManyToManyField('Category', blank=True, verbose_name="Categorias")
    photo = models.ImageField(upload_to='post_photo', verbose_name="Foto", blank=True)
    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

class Comment(models.Model):
    post = models.ForeignKey('Post')
    email = models.EmailField()
    name = models.CharField(max_length=60, verbose_name="Nome")
    comment = models.TextField(verbose_name=u"Comentário")
    approved = models.BooleanField(default = False, verbose_name="Aprovado")
    created_at = models.DateTimeField(auto_now_add = True) 
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u"Comentários"
        verbose_name = u"Comentário"
