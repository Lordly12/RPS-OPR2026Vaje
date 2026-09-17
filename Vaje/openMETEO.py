#https://hackmd.io/@lukac/api1
# izpiši trenutno teperaturo za poljubni kraj
import requests
def trenutna_temp(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto"
    call = requests.get(base_url).json()
    print(call["current"]["temperature_2m"])
trenutna_temp(45.12,14.5)


#Izpiši temperature za naslednjih 7 dni.
def temp_7dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    call = requests.get(base_url).json()
    print(call["hourly"]["temperature_2m"])
temp_7dni(45.12, 14.5)

#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
def temp_7dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    call = requests.get(base_url).json()

    datumi = call["daily"]["time"]
    temperature_max = call["daily"]["temperature_2m_max"]
    temperature_min = call["daily"]["temperature_2m_min"]
    print(temperature_min),(temperature_max)
temp_7dni(45.12, 14.5)


temp_7dni(45.12, 14.5)
#Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.
def temp_7dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    call = requests.get(base_url).json()

    datumi = call["daily"]["time"]
    max_temperatura = call["daily"]["temperature_2m_max"]
    min_temperatura = call["daily"]["temperature_2m_min"]

    najvecja_razlika = max_temperatura[0] - min_temperatura[0]
    dan = datumi[0]

    for i in range(len(datumi)):
        razlika = max_temperatura[i] - min_temperatura[i]
        if razlika > najvecja_razlika:
            najvecja_razlika = razlika
            dan = datumi[i]

    print("Največja razlika je bila:", dan, najvecja_razlika, "°C")

temp_7dni(45.12, 14.5)
#Med 10 največjimi slovenskimi mesti poišči tisto
def trenutna_temperatura2(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast"
    parms = {"latitude" : lat,
             "longitude" : lon,
             "current" : "temperature_2m",
             "timezone" : "auto",
             "forecast_days" : 1
             }
    call = requests.get(base_url,params = parms)
    json = call.json()
    return json["current"]["temperature_2m"]


cities = [("Ljubljana",46.0511,14.5051),
          ("Maribor",46.5538,15.6459),
          ("Celje",46.2309,15.2064),
          ("Kranj",46.2389,14.3556),
          ("Koper",45.5481,13.7302),
          ("Velenje",46.3592,15.1103),
          ("Novo mesto",45.8011,15.1710),
          ("Ptuj",46.4194,15.8697),
          ("Trbovlje",46.1547,15.0536),
          ("Kamnik",46.2259,14.6121)]


for c in cities[:4]:
    print(trenutna_temperatura2(c[1],c[2]),c[0])


#trenutna_temperatura2(45.12,14.5)
#ki bo danes najtoplejše oz. najhladnejše




#ki bo imelo najmanj oz. največ dežja



#ki bo imelo najmanj oz. največ vetra.
