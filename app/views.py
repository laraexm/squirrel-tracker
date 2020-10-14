from django.shortcuts import render

from .models import Squirrel

from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }
    return render(request, 'app/index.html',context)


