from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import ScriptSpinnerUserManager

class ScriptSpinnerUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email address'), unique=True)
    is_subscribed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ScriptSpinnerUserManager()

    def __str__(self):
        return self.email