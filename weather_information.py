
# Following is a project by Kartik Srivardhan enrolled in the Python and Cyber Security Bootcamp by Shape AI.

import requests
import os
from datetime import datetime

api_key = 'dbac61b3c16e1bfd5cc587ba818469e2' #Unique API ID
city = input("Enter the City : ")

# Requesting Data
weather_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
api_link = requests.get(weather_api_link)
api_data = api_link.json()

#Variables to store the received data
city_temp = ((api_data['main']['temp']) - 273.15)
description = api_data['weather'][0]['description']
humdity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# Printing the received data
print ("---------------------------------------------------------------------")
print ("-> Source : OpenWeatherMap.org")
print ("-> Location : ",city.upper())
print ("-> Date and Time : ",date_time)
print ("---------------------------------------------------------------------")

print ("-> Current Temprature : {:.2f} °C".format(city_temp))
print ("-> Weather Description :",description)
print ("-> Humidity :",humdity,"%")
print ("-> Wind Speed :",wind_speed,"Kmph")
print ("---------------------------------------------------------------------")

# Wrinting the received data into a text file
with open("weather.txt", "w+") as f:
    f.write("-> Source : OpenWeatherMap.org\n")
    f.write("-> Location : {}\n".format(city.upper()))
    f.write("-> Date and Time : {}\n\n".format(date_time))
    
    f.write("-> Current Temprature : {:.2f} degree C\n".format(city_temp))
    f.write("-> Weather Description : {}\n".format(description))
    f.write("-> Humidity : {} %\n".format(humdity))
    f.write("-> Wind Speed : {} Kmph".format(wind_speed))
    f.close()

input("Press any key to exit!")
