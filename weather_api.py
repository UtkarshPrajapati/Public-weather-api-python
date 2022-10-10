import requests
noc=input("City: ")
a=""
if not noc:
    a="noc"
    noc="Lucknow"
b=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+noc+"&appid=80034b9f6a1313313b0fde51b165d94e").json()
if len(b)<3:
    print("City's name may be changed or city not found!!")
else:
    if a=="noc":
        print("By Default city: ","Lucknow")
    lat=b["coord"]["lat"]
    lon=b["coord"]["lon"]
    w=b["weather"][0]["main"]
    desc=b["weather"][0]["description"]
    temp=b["main"]["temp"]
    feel=b["main"]["feels_like"]
    print("LAT: "+str(lat)+"  LON: "+str(lon))
    print("TEMP: "+str(temp-273.15)[:4]+"°C")
    print("FEELS LIKE: "+str(feel-273.15)[:4]+"°C")
    print("WEATHER: "+w)
    print("DESCRIPTION: "+desc)
    print("Humidity is: "+str(b["main"]["humidity"])+"%")
