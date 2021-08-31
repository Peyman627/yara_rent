from django.http import Http404
from django.shortcuts import render

from .models import Car


def car_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'rent/car_list.html', context)


def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        raise Http404
    context = {'car': car}
    return render(request, 'rent/car_detail.html', context)
