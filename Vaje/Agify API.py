import requests
# imena = [luka,bine]
# agify
# najdi najstarejše ime iz seznama 
imena = ["Teo","Irena","Sebastajn","Kalin"]
# url = "https://api.agify.io/?name=Teo,Irena,Sebastajn,Kalin"
# foreach
# for i in imena:
#     print(i)


# enumerate(list)
# print(list(enumerate(imena)))
# for i,e in enumerate(imena):
#     print(i,e)


največje = 0
for name in imena:
    starost = requests.get(f"https://api.agify.io/?name={name}").json()['age']
    if starost > največje:
        največje = starost
        največje_ime = name
print(f"najstarejše ime je:{največje_ime}")