import requests

from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import City
from .forms import CityForm


def index(request):
    api_url = "http://api.openweathermap.org/data/2.5/weather/"

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        params = {
            'q': city,
            'appid': '495c22d9e84ffa4065e720761abbcfd8',
            'units': 'metric'
        }

        res = requests.get(api_url, params=params).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)



class WeatherDeleteView(DeleteView):
    model = City
    template_name = 'weather/weather_delete.html'
    success_url = reverse_lazy('home')
