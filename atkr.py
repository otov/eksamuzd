import json
import requests

url="https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=1000"

response = requests.get(url)

if response.status_code == 200:
    dati = response.json()
    print(dati)
    records=dati["result"]["records"]

    print("")
    print("Baterijas un akumulātori:")
    print("")
    for ieraksts in records:
        if ieraksts.get("8 : Baterijas un akumulatori", "").strip().lower()=="x":
            adrese = ieraksts.get("adrese")
            novads = ieraksts.get("pilsetanovads")
            print("Adrese, kur nodod baterijas:", adrese)
            print("Novads, kuros nodod baterijas: ",novads)
            

    print("")
    print("Riepas:")
    print("")
    for ieraksts in records:
        if ieraksts.get("10 : Nolietotās riepas", "").strip().lower()=="x":
            adrese = ieraksts.get("adrese")
            novads = ieraksts.get("pilsetanovads")
            print("Adrese, kur nodod riepas:", adrese)
            print("Novads, kuros nodod riepas: ",novads)
            

    print("")
    print("Metāls:")
    print("")
    for ieraksts in records:
        if ieraksts.get("3 : Metāls", "").strip().lower()=="x":
            adrese = ieraksts.get("adrese")
            novads = ieraksts.get("pilsetanovads")
            print("Adrese, kur nodod metālu:", adrese)
            print("Novads, kuros nodod metālu: ",novads)
            break