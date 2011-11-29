# -*- encoding: utf8 -*-
from django.contrib import admin
from models import Post, Comment, Category
from forms import CommentForm

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at', 'last_modified']
    actions_on_bottom = True
    search_fields = ['title','categories__name']
    inlines = [CommentInline]
    ordering = ['-created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email' ,'comment', 'approved')
    ordering = ['-created_at']
    actions = ['aprovar', 'reprovar']
    def aprovar(self, request, queryset):
        queryset.update(approved = True)
        self.message_user(request, "%d comentarios aprovados com sucesso!"%queryset.__len__())
    aprovar.short_description = "Aprovar comentarios selecionados"
    def reprovar(self, request, queryset):
        queryset.update(approved = False)
        self.message_user(request, "%d comentarios reprovados com sucesso!"%queryset.__len__())
    reprovar.short_description = u"Reprovar comentários selecionados"
        

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
