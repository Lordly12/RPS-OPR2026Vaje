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
temp_7dni(12.3, 21.4)

#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
def temp_7dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    call = requests.get(base_url).json()
    print(call["hourly"]["temperature_2m"])
    for i in temperatura()
        if i > temperatura
temp_7dni(12.3, 21.4)