from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class College(models.Model):
    name = models.CharField(_("College Name"), max_length=256, unique=True)
    contact = models.CharField(_("College Contact Number"), max_length=16)
    location = models.TextField(_("College Location"))
    description = models.TextField(_("College Description"))

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(_("Year Tag"), max_length=50)
    college = models.ForeignKey("college.College", verbose_name=_("College"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Student(User):
    college = models.ForeignKey("college.College", verbose_name=_("College"), on_delete=models.CASCADE)
    batch = models.ForeignKey("college.Batch", verbose_name=_("Batch"), on_delete=models.CASCADE)


class Staff(User):
    is_staff = True
    pass
