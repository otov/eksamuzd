class darbinieks:
    def __init__(self, vards, veids, stundas, alga):
        self.vards=vards
        self.veids=veids
        self.stundas=stundas
        self.alga=alga
    
veids=input(int("Ievadiet darbinieka veidu (Ofisa darbinieks=1 Rūpnīcas darbinieks=2): "))
vards=input(str("Ievadiet darbinieka vārdu: "))
stundas=input(int("Ievadiet darba stundas: "))
alga=input(int("Ievadiet darbinieka stundas algu: "))

if veids==1:
    class ofisadarbinieks(darbinieks):
        def __init__(self, vards, stundas, alga):
            super().__init__(vards,stundas,alga)

        likme=0.2
        opalga=0

        bezkopalga=stundas*alga
        

        print("Ofisa darbinieka vārds: ",vards)
        print("")




elif veids==2:
    class rupnicasdarbinieks(darbinieks):
        def __init__(self, vards, stundas, alga):
            super().__init__(vards,stundas,alga)





else:
    print("Ievadīta nederīga vērtība!")
