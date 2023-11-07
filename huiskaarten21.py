# huiskaarten 21

import random
import time
huisaas = False
speleraas = False
einde = False    

def kaartensysteem():
    global kaarten
    empty = 1
    while empty != 0:
        if huisbeurt == True:
            lstkaarten.remove(str(huiskaartlit))
            kaarten = tuple(lstkaarten)
            empty = len(kaarten)
            break
        elif spelerbeurt == True:
            lstkaarten.remove(str(spelerkaartlit))
            kaarten = tuple(lstkaarten)
            empty = len(kaarten)
            break
        else:
            print("hmm... bug?")
            break

def huisselectie():
    global spelerbeurt
    global huisbeurt
    global huisscore
    global huiskaart
    global huiskaartlit
    global huisaas
    huisbeurt = False
    print()
    time.sleep(3)
    huiskaart = random.choice(kaarten)
    if huiskaart == "A":
        print(f"{huisvoornaam} heeft een aas getrokken.")
        huisaas = True
        huiskaartlit = "A"
        if huisscore >= 11:
            huiskaart = 1
        else:
            huiskaart = 11
    elif huiskaart == "B":
        print(f"{huisvoornaam} heeft een boer ingehuurd.")
        huiskaart = 10
        huiskaartlit = "B"
    elif huiskaart == "V":
        print(f"{huisvoornaam} heeft een vrouw gevonden.")
        huiskaart = 10
        huiskaartlit = "V"
    elif huiskaart == "H":
        print(f"{huisvoornaam} heeft een heer ontmoet.")
        huiskaart = 10
        huiskaartlit = "H"
    else:
        huiskaart = int(huiskaart)
        huiskaartlit = int(huiskaart)
        print(f"{huisvoornaam} heeft een {huiskaart} aan de haak.")
    huisscore += huiskaart
    if huisscore > 21 and huisaas == True:
        huisscore -= 10
    else:
        huisscore -= 0
        huisaas = False
    print()
    time.sleep(2)
    print(f"De totale score van {huisvolnaam} is nu {huisscore}.")
    print()
    spelerbeurt = False
    huisbeurt = True
    kaartensysteem()

def spelerselectie():
    global huisbeurt
    global spelerbeurt
    global spelerscore
    global spelerkaart
    global spelerkaartlit
    global speleraas
    spelerbeurt = False
    print()
    time.sleep(3)
    spelerkaart = random.choice(kaarten)
    if spelerkaart == "A":
        print("Je hebt een aas getrokken.")
        speleraas = True
        spelerkaartlit = "A"
        if spelerscore >= 11:
            spelerkaart = 1
        else:
            spelerkaart = 11
    elif spelerkaart == "B":
        spelerkaartlit = "B"
        print("Je hebt een boer ingehuurd.")
        spelerkaart = 10
    elif spelerkaart == "V":
        print("Je hebt een vrouw gevonden.")
        spelerkaart = 10
        spelerkaartlit = "V"
    elif spelerkaart == "H":
        print("Je hebt een heer ontmoet.")
        spelerkaart = 10
        spelerkaartlit = "H"
    else:
        spelerkaart = int(spelerkaart)
        spelerkaartlit = int(spelerkaart)
        print(f"Je hebt een {spelerkaart} aan de haak.")
    spelerscore += spelerkaart 
    if spelerscore > 21 and speleraas == True:
        spelerscore -= 10
    else:
        spelerscore -= 0
        speleraas = False
    print()
    time.sleep(2)
    print(f"Jouw totale score is nu {spelerscore}.")
    print()
    huisbeurt = False
    spelerbeurt = True
    kaartensysteem()

def ditzijndenamen():
    import time
    from randomname import randomfullname, randomfirstname
    global spelervolnaam
    global spelervoornaam 
    global huisvolnaam
    global huisvoornaam
    while True:
        spelervolnaam = input("Wat is je naam? ")
        if spelervolnaam == "" or spelervolnaam == " ":
            print()
            print("Kom op. Zeg gewoon even netjes hoe je heet, alsjeblieft.")
            print()
            continue
        elif not spelervolnaam.isalpha():
            if spelervolnaam.find("-") or spelervolnaam.find(" ") is True:
                break
            else:
                print()
                print("Kom op. Zeg gewoon even netjes hoe je heet, alsjeblieft.")
                print()
                continue 
        elif len(spelervolnaam) > 35:
            print()
            print("Je naam is te lang... Mag het ook iets korter?")
            print()
        else:
            break
    spelervolnaam = spelervolnaam.title()
    if spelervolnaam.find(" ") == -1:
        spelervoornaam = spelervolnaam
    else:
        spelernaamindex = spelervolnaam.index(" ")
        spelervoornaam = spelervolnaam[:spelernaamindex]
    huisvolnaam = randomfullname 
    huisvoornaam = randomfirstname
    print()
    print()
    time.sleep(1)
    print(f"Welkom, {spelervoornaam}. Je speelt vandaag tegen {huisvolnaam}.")

def huiskaarten21():
    global spelerWtest
    global spelerGtest
    global spelerVtest
    einde = False
    time.sleep(2)
    while True:
        print(f"{huisvoornaam} is aan de beurt.")
        huisselectie()
        if huisscore > 21:
            print(f"{huisvolnaam} heeft verloren met een score van {huisscore}!")
            spelerWtest = True
            break
        elif huisscore == 21:
            print(f"{huisvolnaam} heeft {huisscore} en daarmee heeft {huisvoornaam} gewonnen! Maar onthoud: iedereen is een winnaar...")
            spelerVtest = True
            break
        print()
        time.sleep(3)
        print("Jij bent aan de beurt.")
        spelerselectie()
        if spelerscore > 21:
            print(f"Je hebt verloren met een score van {spelerscore}!")
            spelerVtest = True
            break
        elif spelerscore == 21:
            print(f"Je hebt {spelerscore} en daarmee heb je gewonnen! Maar onthoud: iedereen is een winnaar...")
            spelerWtest = True
            break
        vraag = input("Wil je verder spelen? Antwoord met \"ja\" of \"nee\". ")
        print()
        print()
        if vraag == "ja" or vraag == "Ja" or vraag == "j":
            huisbeslissingrandom = random.randint(0, 1)
            if huisscore < spelerscore:
                huisbeslissing = True
            elif huisscore > 17 and huisaas == False:
                huisbeslissing = False
            elif huisscore > 19 and huisaas == True:
                huisbeslissing = True
            elif huisscore > 11 and huisbeslissingrandom == 1:
                huisbeslissing = True
            elif huisscore > 11 and huisbeslissingrandom == 0 and huisaas == False:
                huisbeslissing = False
            elif huisscore > 11 and huisbeslissingrandom == 0 and huisaas == True:
                huisbeslissing = True
            else:
                huisbeslissing = True
            if huisbeslissing == True:     
                continue
            elif huisbeslissing == False:
                time.sleep(3)
                print(f"{huisvoornaam} is aan de beurt.")
                print()
                time.sleep(2)
                print(f"{huisvoornaam} wil niet verder spelen.")
                print()
                print()
                time.sleep(3)
                print("Jij bent aan de beurt.")
                spelerselectie()        
                while spelerscore < 21:
                    vraag = input("Wil je verder spelen? Antwoord met \"ja\" of \"nee\". ")
                    if vraag == "ja" or vraag == "Ja" or vraag == "j":
                        print()
                        print()
                        time.sleep(3)
                        print("Jij bent aan de beurt.")
                        spelerselectie()   
                        if spelerscore == 21:   
                            print(f"Je hebt {spelerscore} en daarmee heb je gewonnen! Maar onthoud: iedereen is een winnaar...")
                            spelerWtest = True
                            einde = True
                            break                  
                        elif spelerscore > 21:
                            print(f"Je hebt verloren met een score van {spelerscore}!")
                            spelerVtest = True
                            einde = True
                            break              
                        elif huisscore > spelerscore:
                            print()
                            continue
                        elif huisscore < spelerscore:
                            print(f"Je hebt gewonnen met een score van {spelerscore} tegen {huisscore}!")
                            spelerWtest = True
                            einde = True
                            break
                        elif huisscore == spelerscore:
                            print(f"Het is een gelijkspel. Jullie hebben allebei een score van {huisscore}. Saai hoor...")
                            spelerGtest = True
                            einde = True
                            break                 
                    else:
                        if huisscore > spelerscore:
                            print(f"{huisvolnaam} heeft gewonnen met een score van {huisscore} tegen {spelerscore}!")
                            spelerVtest = True
                            einde = True
                            break
                        elif huisscore < spelerscore:
                            print(f"Je hebt gewonnen met een score van {spelerscore} tegen {huisscore}!")
                            spelerWtest = True
                            einde = True
                            break
                        elif huisscore == spelerscore:
                            print(f"Het is een gelijkspel. Jullie hebben allebei een score van {huisscore}. Saai hoor...")
                            spelerGtest = True
                            einde = True
                            break 
                if einde == True:
                    break
                if spelerscore == 21:   
                    print(f"Je hebt {spelerscore} en daarmee heb je gewonnen! Maar onthoud: iedereen is een winnaar...")
                    spelerWtest = True
                    break                  
                elif spelerscore > 21:
                    print(f"Je hebt verloren met een score van {spelerscore}!")
                    spelerVtest = True
                    break              
                elif huisscore > spelerscore:
                    print(f"{huisvolnaam} heeft gewonnen met een score van {huisscore} tegen {spelerscore}!")
                    spelerVtest = True
                    break
                elif huisscore < spelerscore:
                    print(f"Je hebt gewonnen met een score van {spelerscore} tegen {huisscore}!")
                    spelerWtest = True
                    break
                elif huisscore == spelerscore:
                    print(f"Het is een gelijkspel. Jullie hebben allebei een score van {huisscore}. Saai hoor...")
                    spelerGtest = True
                    break
        elif vraag == "nee" or vraag == "Nee" or vraag == "n":
            time.sleep(3)
            print(f"{huisvoornaam} is aan de beurt.")
            huisbeslissingrandom = random.randint(0, 1)
            if huisscore > spelerscore:
                huisbeslissing = False
            elif huisscore < spelerscore:
                huisbeslissing = True
            elif huisscore > 17:
                huisbeslissing = False
            elif huisscore > 11 and huisbeslissingrandom == 1:
                huisbeslissing = True
            elif huisscore > 11 and huisbeslissingrandom == 0:
                huisbeslissing = False
            else:
                huisbeslissing = True
            if huisbeslissing == False:
                print()
                time.sleep(2)
                print(f"{huisvoornaam} wil ook niet verder spelen.")
                print()
                if huisscore > 21:
                    print(f"{huisvolnaam} heeft verloren met een score van {huisscore}!")
                    spelerWtest = True
                    break   
                elif huisscore > spelerscore:
                    print(f"{huisvolnaam} heeft gewonnen met een score van {huisscore} tegen {spelerscore}!")
                    spelerVtest = True
                    break
                elif huisscore < spelerscore:
                    print(f"Je hebt gewonnen met een score van {spelerscore} tegen {huisscore}!")
                    spelerWtest = True
                    break
                elif huisscore == spelerscore:
                    print(f"Het is een gelijkspel. Jullie hebben allebei een score van {huisscore}. Saai hoor...")
                    spelerGtest = True
            else:
                huisselectie()
                while huisscore < spelerscore:
                    print()
                    time.sleep(3)
                    print(f"{huisvoornaam} is aan de beurt.")
                    if huisscore < 21:
                        huisbeslissing = True
                    elif huisscore > spelerscore:
                        huisbeslissing = False
                    if huisbeslissing == False:
                        print()
                        time.sleep(2)
                        print(f"{huisvoornaam} wil ook niet verder spelen.")
                        print()
                        if huisscore > 21:
                            print(f"{huisvolnaam} heeft verloren met een score van {huisscore}!")
                            spelerWtest = True
                        elif huisscore > spelerscore:
                            print(f"{huisvolnaam} heeft gewonnen met een score van {huisscore} tegen {spelerscore}!")
                            spelerVtest = True
                        elif huisscore < spelerscore:
                            print(f"Je hebt gewonnen met een score van {spelerscore} tegen {huisscore}!")
                            spelerWtest = True
                        elif huisscore == spelerscore:
                            print(f"Het is een gelijkspel. Jullie hebben allebei een score van {huisscore}. Saai hoor...")
                            spelerGtest = True
                        einde = True
                        break
                    elif huisbeslissing == True:
                        huisselectie()
                        if huisscore > 21:
                            print(f"{huisvolnaam} heeft verloren met een score van {huisscore}!")
                            spelerWtest = True
                            einde = True
                            break
                        elif huisscore == 21:
                            print(f"{huisvolnaam} heeft {huisscore} en daarmee heeft {huisvoornaam} gewonnen! Maar onthoud: iedereen is een winnaar...")
                            spelerVtest = True
                            einde = True
                            break
                        elif huisscore > spelerscore:
                            print(f"{huisvolnaam} heeft gewonnen met een score van {huisscore} tegen {spelerscore}!")
                            spelerVtest = True
                            einde = True
                            break
                        elif huisscore == spelerscore:
                            print(f"Het is een gelijkspel. Jullie hebben allebei een score van {huisscore}. Saai hoor...")
                            spelerGtest = True
                            einde = True
                            break
                        else:
                            continue
                if einde == True:
                    break
                if huisscore > 21:
                    print(f"{huisvolnaam} heeft verloren met een score van {huisscore}!")
                    spelerWtest = True
                    break   
                elif huisscore > spelerscore:
                    print(f"{huisvolnaam} heeft gewonnen met een score van {huisscore} tegen {spelerscore}!")
                    spelerVtest = True
                    break
                elif huisscore < spelerscore:
                    print(f"Je hebt gewonnen met een score van {spelerscore} tegen {huisscore}!")
                    spelerWtest = True
                    break
                elif huisscore == spelerscore:
                    print(f"Het is een gelijkspel. Jullie hebben allebei een score van {huisscore}. Saai hoor...")
                    spelerGtest = True
                    break
        else:
            vraag = input("Wil je verder spelen? Antwoord met \"ja\" of \"nee\". ")
            print()
            print()

spelerW = 0
spelerG = 0
spelerV = 0
print()
print("Welkom bij Huiskaarten 21!")
print()
print()
ditzijndenamen()
print()
print()
while True:
    huisscore = int(0)
    spelerscore = int(0)
    kaarten = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H")
    lstkaarten = list(kaarten) * 4
    random.shuffle(lstkaarten)
    spelerWtest = False
    spelerGtest = False
    spelerVtest = False
    huiskaarten21()
    if spelerWtest == True:
        spelerW += 1
    elif spelerGtest == True:
        spelerG += 1
    elif spelerVtest == True:
        spelerV += 1
    else:
        pass
    print()
    print()
    print(f"{spelervoornaam}, je hebt {spelerW} keer gewonnen en {spelerV} keer verloren van {huisvoornaam}. Jullie hebben {spelerG} keer gelijkgespeeld.")
    print()
    spelen = input("Wil je nog een keer spelen? Antwoord met \"ja\" of \"nee\". ")
    print()
    while True:
        if spelen == "ja" or spelen == "Ja" or spelen == "j":
            print()
            break
        elif spelen == "nee" or spelen == "Nee" or spelen == "n":
            einde = True
            break
        else:
            spelen = input("Wil je nog een keer spelen? Antwoord met \"ja\" of \"nee\". ")
            print()
            continue
    if einde == True:
        print()
        print("Tot ziens!")
        print()
        break

# tauva forever