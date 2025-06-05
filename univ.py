import requests

url="http://universities.hipolabs.com/search?country=Latvia"
response=requests.get(url)

if response.status_code==200:
    dati = response.json()
    print(dati)
    
    print("Latvijas universitātes: ")

    saraksts=[]
    
    print("____________________________________")

    for universitates in dati:
        saraksts.append(universitates.get("name"))

    saraksts.sort

    for nosaukums in saraksts:
        print(nosaukums)

    