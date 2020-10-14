from django.db import models

from django.utils.translation import gettext as _


# Create your models here.

class Squirrel(models.Model):

    X_Latitude = models.FloatField(
        help_text=_('X-Latitude of Squirrel'),
        default = None
    )

    Y_Longitude = models.FloatField(
        help_text=_('Y-Longitude of Squirrel'),
        default = None
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        help_text =_( 'Unique ID of squirrel'),
        default = None
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
        default = AM
    )

    Date = models.DateField(
        help_text=_('Date of record'),
        default = None
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    )

    age = models.CharField(
        max_length=15,
        help_text=_('Age of squirrel'),
        choices=AGE_CHOICES,
        blank=True,
        null=True,
        default = ADULT
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    WHITE = 'White'

    COLOR_CHOICES_PRIMARY = (
        (GRAY,_( 'Gray')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
    )

    COLOR_CHOICES_HIGHLIGHT = (
        (GRAY, _('Gray')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
        (WHITE, _('White')),
    )

    Primary_Fur_Color = models.CharField(
        max_length=15,
        help_text=_('Primary fur color of squirrel'),
        choices=COLOR_CHOICES_PRIMARY,
        blank=True,
        null=True,
        default = GRAY
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, _('Ground Plane')),
        (ABOVE_GROUND, _('Above Ground')),
    )
    
    Location = models.CharField(
        max_length=50,
        help_text=_('Location of squirrel'),
        choices=LOCATION_CHOICES,
        blank=True,
        null=True,
        default = GROUND_PLANE
    )

    Specific_Location = models.CharField(
        max_length=50,
        help_text=_('Specific location of squirrel'),
        blank=True,
        null=True,
        default = None
    )

    Running = models.BooleanField(
        help_text=_('Is the squirrel running?'),
        default = False
    )

    Chasing = models.BooleanField(
        help_text=_('Is the squirrel chasing?'),
        default = False
    )  

    Climbing = models.BooleanField(
        help_text=_('Is the squirrel climbing?'),
        default = False
    )

    Eating = models.BooleanField(
        help_text=_('Is the squirrel eating?'),
        default = False
    )

    Foraging = models.BooleanField(
        help_text=_('Is the squirrel foraging?'),
        default = False
    )

    Other_Activity = models.TextField(
        blank=True,
    )

    Kuks = models.BooleanField(
        help_text=_('Does the squirrel have kuks?'),
        default = False
    )

    Quaas = models.BooleanField(
        help_text=_('Does the squirrel have quaas?'),
        default = False
    )

    Moans = models.BooleanField(
        help_text=_('Does the squirrel have moans?'),
        default = False
    )

    Tail_Flags = models.BooleanField(
        help_text=_('Does the squirrel have tail flags?'),
        default = False
    )

    Tail_Twitches = models.BooleanField(
        help_text=_('Does the squirrel have tail twitches?'),
        default = False
    )

    Approaches = models.BooleanField(
        help_text=_('Does the squirrel have approaches?'),
        default = False
    )

    Indifferent = models.BooleanField(
        help_text=_('Is the squirrel indifferent?'),
        default = False
    )

    Runs_From = models.BooleanField(
        help_text=_('Does the squirrel run from?'),
        default = False
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
