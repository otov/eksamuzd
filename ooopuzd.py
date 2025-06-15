class darbinieks:
    def __init__(self, vards, veids, stundas, alga):
        self.vards=vards
        self.veids=veids
        self.stundas=stundas
        self.alga=alga
    
veids=input("Ievadiet darbinieka veidu (Ofisa darbinieks=1 Rūpnīcas darbinieks=2): ")
vards=input("Ievadiet darbinieka vārdu: ")
stundas=int(input("Ievadiet darba stundas: "))
alga=int(input("Ievadiet darbinieka stundas algu: "))

if veids=="1":
    class ofisadarbinieks(darbinieks):
        def __init__(self, vards, stundas, alga):
            super().__init__(vards,stundas,alga)

        likme=0.8
        bezkopalga=0
        arkopalga=0
        bezkopalga=stundas*alga
        arkopalga=bezkopalga*likme

        print("Ofisa darbinieka vārds: ",vards)
        print("Ofisa darbinieka nostrādātās stundas: ",stundas)
        print("Ofisa darbinieka stundas alga: ",alga)
        print("Ofisa darbinieka bruto alga:",bezkopalga)
        print("Ofisa darbinieka neto alga: ",arkopalga)


elif veids=="2":
    class rupnicasdarbinieks(darbinieks):
        def __init__(self, vards, stundas, alga):
            super().__init__(vards,stundas,alga)


        nakts=input(str("Vai rūpnīcas darbinieks strādā nakts maiņu (Jā vai Nē): "))
        likme=0.8
        likme2=1.1
        bezkopalga2=0
        arkopalga2=0
        if nakts=="Jā" or "Ja" or "jā" or "ja":
            
            bezkopalga2=(stundas*alga)*likme2
            arkopalga2=bezkopalga2*likme

            print("Rūpnīcas darbinieka vārds: ",vards)
            print("Rūpnīcas darbinieka nostrādātās stundas: ",stundas)
            print("Rūpnīcas darbinieka bruto alga: ", bezkopalga2)
            print("Rūpnīcas darbinieka bruto alga: ", arkopalga2)


        elif nakts== "Nē" or "Ne" or "nē" or "ne":
            bezkopalga2=stundas*alga
            arkopalga2=bezkopalga2*likme
            
            print("Rūpnīcas darbinieka vārds: ",vards)
            print("Rūpnīcas darbinieka nostrādātās stundas: ",stundas)
            print("Rūpnīcas darbinieka bruto alga: ", bezkopalga2)
            print("Rūpnīcas darbinieka bruto alga: ", arkopalga2)

        else:
            print("Ievadīta nederīga vērtība")
            


else:
    print("Ievadīta nederīga vērtība!")
