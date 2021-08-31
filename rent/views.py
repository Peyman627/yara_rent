from django.shortcuts import get_list_or_404, render, get_object_or_404

from .models import Car


def car_list(request):
    cars = get_list_or_404(Car)
    context = {'cars': cars}
    return render(request, 'rent/car_list.html', context)


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {'car': car}
    return render(request, 'rent/car_detail.html', context)
