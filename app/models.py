from django.db import models

from django.utils.translation import gettext as _


# Create your models here.

class Squirrel( models.Model):
    def __str__(self):
        return self.unique_id

    unique_id = models.CharField(
        max_length=100,
        help_text = 'Unique ID of squirrel',
        )


