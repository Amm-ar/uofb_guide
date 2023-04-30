from django.contrib import admin
from .models import Calendar, Event, Exceptions, AcademicYear

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'importance', 'year_tag', 'added_at']
    search_fields = ['title', 'description__contains']
    list_filter = ['year_tag']
    

@admin.register(Exceptions)
class ExceptionsAdmin(admin.ModelAdmin):
    pass


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    pass
