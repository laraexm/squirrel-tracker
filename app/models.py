from django.db import models

from django.utils.translation import gettext as _


# Create your models here.

class Squirrel(models.Model):
    X_Latitude = models.FloatField(
        max_digits=100,
        decimal_places=10,
        help_text=_('X-Latitude of Squirrel'),
    )

    Y_Longitude = models.FloatField(
        max_digits=100,
        decimal_places=10,
        help_text=_('Y-Longitude of Squirrel'),
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        help_text = 'Unique ID of squirrel',
        )

    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = [
            (PM, _('PM')),
            (AM, _('AM')),
    ]

    Shift = models.CharField(
        max_length=2,
        help_text=_('Shift of squirrel'),
        choices=SHIFT_CHOICES,
    )

    Date = models.DateField(
        help_text=_(''),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
        max_length=15,
        help_text=_('Age of squirrel'),
        choices=AGE_CHOICES,
        blank=True,
        null=True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES_PRIMARY = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )

    COLOR_CHOICES_HIGHLIGHT = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (WHITE, 'White'),
    )

    Primary_Fur_Color = models.CharField(
        max_length=15,
        help_text=_('Primary fur color of squirrel'),
        choices=COLOR_CHOICES_PRIMARY,
        blank=True,
        null=True,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    )
    
    Location = models.CharField(
        max_length=15,
        help_text=_('Location of squirrel'),
        choices=LOCATION_CHOICES,
        blank=True,
        null=True,
    ）

    Specific_Location = models.CharField(
        max_length=15,
        help_text=_('Specific location of squirrel'),
        blank=True,
        null=True,
    )

    Running = models.BooleanField(
        help_text=_('Is the squirrel running?'),
    )

    Chasing = models.BooleanField(
        help_text=_('Is the squirrel chasing?'),
    )  

    Climbing = models.BooleanField(
        help_text=_('Is the squirrel climbing?'),
    )

    Eating = models.BooleanField(
        help_text=_('Is the squirrel eating?'),
    )

    Foraging = models.BooleanField(
        help_text=_('Is the squirrel foraging?'),
    )

    Other_Activity = models.TextField(
        blank=True,
    )

    Kuks = models.BooleanField(
        help_text=_('Does the squirrel have kuks?'),
    )

    Quaas = models.BooleanField(
        help_text=_('Does the squirrel have quaas?'),
    )

    Moans = models.BooleanField(
        help_text=_('Does the squirrel have moans?'),
    )

    Tail_Flags = models.BooleanField(
        help_text=_('Does the squirrel have tail flags?'),
    )

    Tail_Twitches = models.BooleanField(
        help_text=_('Does the squirrel have tail twitches?'),
    )

    Approaches = models.BooleanField(
        help_text=_('Does the squirrel have approaches?'),
    )

    Indifferent = models.BooleanField(
        help_text=_('Is the squirrel indifferent?'),
    )

    Runs_From = models.BooleanField(
        help_text=_('Does the squirrel run from?'),
    )

    def __str__(self):
        return self.unique_id
