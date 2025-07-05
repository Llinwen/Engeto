ukoly = []
#Funkce přidá nový úkol do seznamu, zadá jeho název a popis dle vstupu od uživatele
def pridat_ukol():
    while True:
        nazev_ukolu=input("\nZadejte název úkolu: ").strip()
        while not nazev_ukolu:
            nazev_ukolu=input("Zadali jste prázdný název úkolu. Prosím zadejte znovu: ").strip()
        popis_ukolu=input("Zadejte popis úkolu: ").strip() 
        if not popis_ukolu:
            print("Zadali jste prázdný popis úkolu. Začneme znovu.")
            continue
        novy_ukol={nazev_ukolu:popis_ukolu}
        ukoly.append(novy_ukol)
        print(f"\nÚkol '{nazev_ukolu}' byl přidán.\n")
        break
#Funkce vypíše pořadí, název a popis všech úkolů ze seznamu
def zobrazit_ukoly():
    if ukoly:
        print("\nSeznam úkolů:")
        for poradi_ukolu, ukol in enumerate(ukoly, start=1):     #pořadí úkolu začínáme číslovat od 1
            for nazev_ukolu, popis_ukolu in ukol.items():
                print(f"{poradi_ukolu}. {nazev_ukolu} - {popis_ukolu}")  
        print()
    else:
        print("\nMomentálně tu nejsou žádné úkoly.\n")
#Funkce odstraní zvolený úkol, uživatel vybírá podle pořadí úkolu
def odstranit_ukol():
    if not ukoly:
        print("\nMomentálně tu nejsou žádné úkoly k mazání.\n")
        return
    zobrazit_ukoly()
    while True:
        try:
            mazany_ukol=int(input("Zadejte číslo úkolu, který chcete odstranit: ")) 
            if mazany_ukol <= len(ukoly) and mazany_ukol > 0:
                smazany_ukol=ukoly.pop(mazany_ukol -1)
                nazev_ukolu=list(smazany_ukol.keys())[0]
                print(f"\nÚkol č. {mazany_ukol} '{nazev_ukolu}' byl odstraněn.\n")
                break
            elif mazany_ukol > len(ukoly):
                print("Chyba. Pokoušíte se smazat neexistující úkol.")
            else:
                print("Chyba. Zadejte platné číslo úkolu.")
        except ValueError:
            print("Chyba. Zadejte prosím celé kladné číslo.")
#Funkce zobrazí Hlavní menu po správu a zpracovává výběr uživatele
def hlavni_menu():
    while True:
        print("Správce úkolů: Hlavní menu\n" \
        "1. Přidat nový úkol\n" \
        "2. Zobrazit všechny úkoly\n" \
        "3. Odstranit úkol\n" \
        "4. Konec programu")
        vybrana_moznost=input("Vyberte možnost (1-4): ")
        while vybrana_moznost not in ("1", "2", "3", "4"):
            vybrana_moznost=input("Prosím vyberte platnou možnost (1-4): ")
        if vybrana_moznost=="1":
            pridat_ukol()
        elif vybrana_moznost=="2":
            zobrazit_ukoly()
        elif vybrana_moznost=="3":
            odstranit_ukol()
        elif vybrana_moznost=="4":
            print("\nKonec programu.")
            break
hlavni_menu()
