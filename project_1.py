ukoly = []
def pridat_ukol():
    nazev_ukolu=input("\nZadejte název úkolu: ")
    nazev_ukolu=nazev_ukolu.strip()
    while not nazev_ukolu:
        nazev_ukolu=input("Zadali jste prázdný název úkolu. Prosím zadejte znovu: ")
    popis_ukolu=input("Zadejte popis úkolu: ")
    popis_ukolu=popis_ukolu.strip()
    while not popis_ukolu:
        print("Zadali jste prázdný popis úkolu. Začneme znovu.")
        pridat_ukol()
        return
    ukol={nazev_ukolu:popis_ukolu}
    ukoly.append(ukol)
    print(f"Úkol '{nazev_ukolu}' byl přidán.\n")
def zobrazit_ukoly():
    if ukoly:
        print("\nSeznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):
            for key, value in ukol.items():
                print(f"{index}. {key} - {value}") 
        print()
    if not ukoly:
        print("\nMomentálně tu nejsou žádné úkoly.\n")
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
                key=list(smazany_ukol.keys())[0]
                print(f"Úkol č. {mazany_ukol} '{key}' byl odstraněn.\n")
                break
            elif mazany_ukol > len(ukoly):
                print("Chyba. Pokoušíte se smazat neexistující úkol.")
            else:
                print("Chyba. Zadejte platné číslo úkolu.")
        except ValueError:
            print("Chyba. Zadejte prosím celé kladné číslo.")
def hlavni_menu():
    print("Správce úkolů: Hlavní menu\n" \
    "1. Přidat nový úkol\n" \
    "2. Zobrazit všechny úkoly\n" \
    "3. Odstranit úkol\n" \
    "4. Konec programu")
    user_input=input("Vyberte možnost (1-4): ")
    while user_input not in ("1", "2", "3", "4"):
        user_input=input("Prosím vyberte platnou možnost (1-4): ")
    if user_input=="1":
        pridat_ukol()
        hlavni_menu()
    elif user_input=="2":
        zobrazit_ukoly()
        hlavni_menu()
    elif user_input=="3":
        odstranit_ukol()
        hlavni_menu()
    elif user_input=="4":
        print("\nKonec programu.")
hlavni_menu()
