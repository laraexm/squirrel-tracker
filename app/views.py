from django.shortcuts import render

from .models import Squirrel

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from .forms import CreateNewForm

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

def update_sighting(request, squirrel_id):
    obj = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    form = CreateNewForm(request.POST or None, instance=obj)
    if request.method  == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    return render(request, 'app/update.html', {'form': form})    

def create_new_sighting(request):
    if request.method  == 'POST':
        form = CreateNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = CreateNewForm()
        return render(request, 'app/create_new.html', {'form': form})


