import requests
b=requests.get("https://api.openweathermap.org/data/2.5/weather?q=lucknow&appid=6ba5d1118fe06f144b61869aa6b272c7").json()
name=b["name"]
lat=b["coord"]["lat"]
lon=b["coord"]["lon"]
w=b["weather"][0]["main"]
desc=b["weather"][0]["description"]
temp=b["main"]["temp"]
feel=b["main"]["feels_like"]
print("CITY: "+name)
print("LAT: "+str(lat)+" LON: "+str(lon))
print("TEMP: "+str(temp-273.15))
print("FEELS LIKE: "+str(feel-273.15))
print("WEATHER: "+w)
print("DESCRIPTION: "+desc)

