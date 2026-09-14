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

    najtoplejsi = temperature_max.index(max(temperature_max))
    najhladnejsi = temperature_min.index(min(temperature_min))

    print("Najtoplejši dan:", datumi[najtoplejsi], temperature_max[najtoplejsi], "°C")
    print("Najhladnejši dan:", datumi[najhladnejsi], temperature_min[najhladnejsi], "°C")
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


