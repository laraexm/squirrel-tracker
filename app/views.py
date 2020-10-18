from django.shortcuts import render

from .models import Squirrel

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from .forms import CreateNewForm

from .forms import UpdateForm

from django.http import HttpResponse

# Create your views here.

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }
    return render(request, 'app/index.html',context)

def detail(request,Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)

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

def update_sighting(request, Unique_Squirrel_ID):
    obj = Squirrel.objects.filter(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method  == 'POST':
        form = UpdateForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/sightings/')
    else:
        form = UpdateForm()
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


