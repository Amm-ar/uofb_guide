from django.contrib import admin
from .models import Article, Anouncement


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'author']
    search_fields = ['title', 'body__contains']
    list_filter = ['author']


@admin.register(Anouncement)
class AnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'unit']
    search_fields = ['title', 'body__contains']
    list_filter = ['unit']


