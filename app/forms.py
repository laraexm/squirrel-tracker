from django.forms import ModelForm
from django.views.generic.edit import UpdateView
from .models import Squirrel

class CreateNewForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'

class UpdateForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
            'X_Latitude',
            'Y_Longitude',
            'Unique_Squirrel_ID',
            'Shift',
            'Date',
            'Age',
        ]
