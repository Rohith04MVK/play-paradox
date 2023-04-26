from django.shortcuts import render, redirect
from .forms import RaceTimeForm
from .models import RaceTime


def add_race_time(request):
    if request.method == 'POST':
        form = RaceTimeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('race_time_list')
    else:
        form = RaceTimeForm()
    return render(request, 'add_race_time.html', {'form': form})


def race_time_list(request):
    race_times = RaceTime.objects.all()
    return render(request, 'race_time_list.html', {'race_times': race_times})
