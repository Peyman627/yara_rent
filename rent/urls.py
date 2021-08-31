from django.urls import path

from . import views

app_name = 'rent'

urlpatterns = [
    path('car-list/', views.CarListView.as_view(), name='car_list'),
    path('car-list/<int:pk>', views.CarDetailView.as_view(),
         name='car_detail'),
]