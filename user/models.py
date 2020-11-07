import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import ScriptSpinnerUserManager

class ScriptSpinnerUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email address'), unique=True)
    paid_until = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ScriptSpinnerUserManager()

    def __str__(self):
        return self.email
    
    def set_paid_until(self, date_or_timestamp):
        if isinstance(date_or_timestamp, int):
            # input date as timestamp integer
            paid_until = date.fromtimestamp(date_or_timestamp)
        elif isinstance(date_or_timestamp, str):
            # input date as timestamp string
            paid_until = date.fromtimestamp(int(date_or_timestamp))
        else:
            paid_until = date_or_timestamp

        self.paid_until = paid_until
        self.save()

    def has_paid(self, current_date=datetime.date.today()):
        if self.paid_until is None:
            return False

        return current_date < self.paid_until