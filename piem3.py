def parbaudit_stipendiju(vards, vid_atzime):
    if vid_atzime >= 8: #pirmais sazarojums un nosacījums
        print(vards,"saņem stipendiju.")
    elif vid_atzime >= 6: #otrais sazarojums un nosacījums
        print(vards,"turpina studijas bez stipendijas.")
    else: #visas pārējās iespējas
        print(vards,"jāatkārto kurss.")

vards = input("Ievadiet vārdu: ")
vid_atzime = float(input("Ievadiet vidējo atzīmi: "))

parbaudit_stipendiju(vards, vid_atzime)


