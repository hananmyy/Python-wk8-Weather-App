from django.shortcuts import render
import urllib.request
import json

def index(request):
    data = {}  # Initialize an empty context dictionary
    if request.method == 'POST':
        city = request.POST['city']
        try:
            # Fetch weather data
            source = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=03f8dacf25de3755bd81af5d1adef3e7'
            ).read()
            list_of_data = json.loads(source)

            # Populate the data dictionary
            data = {
                "country_code": list_of_data['sys']['country'],
                "coordinate": f"{list_of_data['coord']['lon']}, {list_of_data['coord']['lat']}",
                "temp": f"{list_of_data['main']['temp']} °C",
                "pressure": list_of_data['main']['pressure'],
                "humidity": list_of_data['main']['humidity'],
                "main": list_of_data['weather'][0]['main'],
                "description": list_of_data['weather'][0]['description'],
                "icon": list_of_data['weather'][0]['icon'],
            }
        except Exception as e:
            # Handle any errors (e.g., city not found)
            data['error'] = "City not found. Please try again."

    # Pass data as context to the template
    return render(request, "main/index.html", {"data": data})
