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

def detail(request,squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel_id)

    context = {
            'squirrel': squirrel,
    }
    return render(request, 'app/detail.html', context)

def map(request):
    squirrels = Squirrel.objects.all()
    plot = Squirrel.objects.order_by('?')[:100]
    context = {
            'squirrels': plot,
            }
    return render(request, 'app/map.html',context)
