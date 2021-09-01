from django.views import generic

from .models import Car


class CarListView(generic.ListView):
    template_name = 'rent/car_list.html'
    queryset = Car.objects.all()
    context_object_name = 'cars'


class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'rent/car_detail.html'
    context_object_name = 'car'
