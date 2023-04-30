from django.db import models
from django.db.utils import OperationalError
from django.utils.translation import ugettext_lazy as _

class AcademicYear(models.Model):
    name = models.CharField(_("Year Tag"), max_length=50) # 2022/2023 and so on

    def __str__(self):
        return self.name
    

class Calendar(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateField()
    

class Event(models.Model):
    title = models.CharField(_("Title"), max_length=50) # Event Title # Example : Start of the Academic Year
    description = models.TextField(_("Description")) # Event Description # Short description of the event
    date = models.DateTimeField(_("Event Date"), auto_now=False, auto_now_add=False) # Event Date
    added_at = models.DateTimeField(_("Date"), auto_now=False, auto_now_add=False) # Event Added At
    importance = models.IntegerField(_("Event Importance")) # Importance
    year_tag = models.ForeignKey("year_calendar.AcademicYear", verbose_name=_("Year"), on_delete=models.CASCADE) # Year Tag # Each Year Should Have a Tag which is the Academic Year Date. Example 2022/2023 



    def __str__(self):
        return self.title
    

class Exceptions(models.Model):
    original_date = models.DateTimeField(_("Original Date"), auto_now=False, auto_now_add=False)
    date = models.DateTimeField(_("Date"), auto_now=False, auto_now_add=False) # Event Date
    event = models.ForeignKey("year_calendar.Event", verbose_name=_("Event"), on_delete=models.CASCADE)

    def __str__(self):
        return self.event
