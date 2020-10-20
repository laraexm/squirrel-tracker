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

def map(request):
    squirrels = Squirrel.objects.all()
    plot = Squirrel.objects.order_by('?')[:100]
    context = {
            'plot': plot,
            }
    return render(request, 'app/map.html',context)

def update_sighting(request, Unique_Squirrel_ID):
    instance = get_object_or_404(Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method  == 'POST':
        form = UpdateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
        else:
            return render(request, 'app/update.html', {'form':'form.errors'})
    else:
        form = UpdateForm(instance=instance)
        return render(request, 'app/update.html', {'form': form})    

def create_new_sighting(request):
    if request.method  == 'POST':
        form = CreateNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
        else:
            return render(request, 'app/create_new.html', {'form':'form.errors'})
    else:
        form = CreateNewForm()
        return render(request, 'app/create_new.html', {'form': form})

def stats(request):
    squirrels = Squirrel.objects.all()
    total_number = len(squirrels)
    am_shift = Squirrel.objects.filter(Shift='AM').count()
    adult_count = Squirrel.objects.filter(Age='Adult').count()
    gray_count = Squirrel.objects.filter(Primary_Fur_Color = 'Gray').count()
    ground_count = Squirrel.objects.filter(Location = 'Ground Plane').count()

    context = {
            'total_number': total_number,
            'am_shift': am_shift,
            'adult_count': adult_count,
            'gray_count': gray_count,
            'ground_count': ground_count,
            }
    return render(request, 'app/stats.html',context)
