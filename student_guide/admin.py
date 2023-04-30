from django.contrib import admin
from .models import GuideEntry

@admin.register(GuideEntry)
class GuideEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created', 'updated']
    search_fields = ['title', 'content__contains']
    list_filter = ['title']
