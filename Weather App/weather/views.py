import datetime
import requests
import os
from django.shortcuts import render
from collections import defaultdict

def home(request):
    # Get name (optional) and city (mandatory)
    name = request.POST.get('name') if request.method == "POST" else None
    city = request.POST.get('city') if request.method == "POST" else None

    weather_data = None
    daily_forecast = []

    if city:
        try:
            # Use API key from Api_Key.txt inside weather folder
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            API_KEY = open(os.path.join(BASE_DIR, "Api_Key.txt"), "r").read().strip()

            current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
            # Use 5-day forecast API instead of One Call
            forecast_url = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"

            # Fetch current weather
            response = requests.get(current_weather_url.format(city, API_KEY)).json()

            if response.get("cod") != 200 and response.get("cod") != "200":
                weather_data = {"city": city, "temperature": "N/A", "description": "City not found or API error.", "icon": "01d"}
            else:
                lat, lon = response['coord']['lat'], response['coord']['lon']
                current_time = datetime.datetime.now()
                weather_data = {
                    "city": city,
                    "temperature": round(response['main']['temp'] - 273.15, 2),
                    "description": response['weather'][0]['description'],
                    "icon": response['weather'][0]['icon'],
                    "current_date": current_time.strftime('%A, %B %d, %Y'),  # Full date
                    "current_time": current_time.strftime('%I:%M %p'),  # Time with AM/PM
                    "current_day": current_time.strftime('%A'),  # Day name
                    "current_short_date": current_time.strftime('%a, %b %d')  # Short date format
                }

                # Fetch 5-day forecast (3-hour intervals)
                forecast_response = requests.get(forecast_url.format(city, API_KEY)).json()
                
                # Group forecasts by day
                daily_data = defaultdict(list)
                for forecast in forecast_response.get('list', []):
                    date = datetime.datetime.fromtimestamp(forecast['dt'])
                    daily_data[date.strftime('%Y-%m-%d')].append(forecast)
                
                # Process each day's data
                for date_str, forecasts in list(daily_data.items())[:7]:  # Get first 7 days
                    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                    temps = [round(f['main']['temp'] - 273.15, 2) for f in forecasts]
                    min_temp = min(temps)
                    max_temp = max(temps)
                    
                    # Get the most common weather condition for the day
                    weather_counts = {}
                    for f in forecasts:
                        desc = f['weather'][0]['description']
                        weather_counts[desc] = weather_counts.get(desc, 0) + 1
                    
                    most_common_desc = max(weather_counts.items(), key=lambda x: x[1])[0]
                    icon = forecasts[0]['weather'][0]['icon']  # Use icon from first forecast of the day
                    
                    daily_forecast.append({
                        "date": date_obj,  # Pass date object instead of string
                        "date_str": date_str,  # Keep string version as well
                        "day_name": date_obj.strftime('%A'),  # Full day name
                        "short_day_name": date_obj.strftime('%a'),  # Short day name
                        "formatted_date": date_obj.strftime('%b %d'),  # Formatted date
                        "temp": min_temp,
                        "max_temp": max_temp,
                        "description": most_common_desc,
                        "icon": icon
                    })
                    
        except Exception as e:
            current_time = datetime.datetime.now()
            weather_data = {
                "city": city, 
                "temperature": "N/A", 
                "description": f"Could not fetch weather. Error: {str(e)}", 
                "icon": "01d",
                "current_date": current_time.strftime('%A, %B %d, %Y'),
                "current_time": current_time.strftime('%I:%M %p'),
                "current_day": current_time.strftime('%A'),
                "current_short_date": current_time.strftime('%a, %b %d')
            }

    else:
        # Add current time even when no city is searched
        current_time = datetime.datetime.now()
        weather_data = {
            "current_date": current_time.strftime('%A, %B %d, %Y'),
            "current_time": current_time.strftime('%I:%M %p'),
            "current_day": current_time.strftime('%A'),
            "current_short_date": current_time.strftime('%a, %b %d')
        } if not weather_data else weather_data

    return render(request, 'index.html', {
        "name": name,
        "weather_data": weather_data,
        "daily_forecast": daily_forecast
    })