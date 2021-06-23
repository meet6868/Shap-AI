import requests
#import os
from datetime import datetime

key = 'cf3bef5397cedf058eaa0b35ae41469f'
loc = input("Enter the city name: ")
api_link = "https://api.openweathermap.org/data/2.5/weather?q="+loc+"&appid="+key
link = requests.get(api_link)
data = link.json()

#create variables to store and display data
temp_city = ((data['main']['temp']) - 273.15)
weather_desc = data['weather'][0]['description']
hmdt = data['main']['humidity']
wind_spd = data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


f=open("D://output.txt","a")
f.write("NEW DATA:-\n\n")
f.write("-------------------------------------------------------------\n")
f.write("Weather Stats for - {}  || {}\n".format(loc.upper(), date_time))
f.write("-------------------------------------------------------------\n")
f.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
f.write("Current weather desc  {}:\n".format(weather_desc))
f.write("Current Humidity      : {}%\n".format(hmdt))
f.write("Current wind speed    :{}kmph\n\n\n\n\n".format(wind_spd ))

f.close();

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(loc.upper(), date_time))
print ("-------------------------------------------------------------")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
