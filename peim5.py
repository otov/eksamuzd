class Students:
    def __init__(self, vards, vid_atzime):
        self.vards = vards
        self.vid_atzime = vid_atzime

    def parbaudit_stipendiju(self):
        if self.vid_atzime >= 8:
            print(self.vards,"saņem stipendiju.")
        else:
            print(self.vards,"nesaņem stipendiju.")

students1 = Students("Jānis", 8.5)
students1.parbaudit_stipendiju()

