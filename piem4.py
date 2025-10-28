studenti = {"Anna": 8, "Jānis": 5, "Laura": 7, "Mārtiņš": 6}

for vards, atzime in studenti.items(): #cikla definēšana
    if atzime >= 6:
        print(f"{vards} ir nokārtojis/usi eksāmenu.")
    else:
        print(f"{vards} nav nokārtojis/usi eksāmenu.")


