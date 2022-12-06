import csv

# výpočet sedmidenního průtoku
# načtení souboru a uložení potřebných údajů do seznamů 

# otevření souboru pro čtení 
with open ("vstup.csv", encoding="utf-8", newline='') as f: #,\
    
    reader=csv.reader(f, delimiter=",")
    
    # vytvoření prázdných seznamů 'a' a 'b', definice proměnné průtok
    prutoky=[]
    radky=[]
    prutok=0

    # uložení řádky a průtoku do proměnné
    for row in reader:
        prutoky.append(row[-1])
        radky.append(row)
        try:
            prutok+= float(row[-1])
        except ValueError:
            pass
    
# definice 'n' (počet hodnot průtoků v seznamu) a 'y' (definice počtu iterací)
n=int(len(prutoky))
y=7 

# otevření souboru pro zápis 
with open ("vystup_7dni.csv","w",encoding="utf-8", newline='') as fout:
    writer = csv.writer (fout)
    
    # dokud je počet prvků v seznamu 7 a více, provádí se výpočet sedmidenního průměru průtoku 
    while n >=y:
        cislo=0

        # extrakce prvního dne ze sedmi dnů, pro které je počítán průměr
        radek=radky.pop (0)
        rada=(radek[0],radek[1],radek[2])
        
        # načítání jednotlivých průtoků do proměnné číslo
        for z in range (y):
            cislo+=float(prutoky.pop(0))
        
        # odebrání nepotřebných řádků 
        for u in range (6):
            radek=radky.pop (0)
        
        # vypsání výsledku do souboru 
        outrow = [rada [0],rada [1],rada [2],round (cislo/7, 4)]
        writer.writerow(outrow)
        n=int(len (prutoky))
    
    # pokud je počet hodnot průtoku v seznamu menší než 7, počítá se průměr z těchto zbylých hodnot 

    # extrakce prvního dne 
    try:
        radek = radky.pop (0)
        rada=(radek[0],radek[1],radek[2])

    
    # definice proměnné i, která udává počet provedených iterací 
        i=0
        cislo=0

    # dokud není seznam prázdný, budou se průtoky připočítávat do proměnné číslo, následně se vydělí počtem hodnot (počet iterací)
        while n>0:
            cislo+=float(prutoky.pop (0))
            n=int(len (prutoky))
            i=i+1
    except IndexError:
        pass
            

    # průměrný průtok posledních dní se vypočítá v proměnné outrow a zapíše se do souboru 
    outrow = [rada [0],rada [1],rada [2],round (cislo/7, 4)]
    writer.writerow(outrow)
    



# výpočet průměrného ročního průtoku 

# otevření souboru s daty pro čtení 
with open ("vstup.csv", encoding="utf-8", newline='') as f:
    
    reader=csv.reader(f, delimiter=",")
    
    # vytvoření seznamů pro uložení roků a řádků
    roky=[]
    radky=[]

    # vyextrahování řádků a roků a načtení do seznamů radky a roky 
    for row in reader: 
        radek=(row[:3])
        radky.append (radek) 

        datum_m=(row[2])
        roky.append (int(datum_m[-4:]))
        
    # odebrání prvního roku a převedení do proměnné rok 
    prvni_rok = roky.pop(0)
    rok=int(prvni_rok)
    
    # odebrání prvního řádku a uložení prvních tří atributů do proměnné prvni rada
    prvni_radek=[]
    prvni_radek = radky.pop(0)
    prvni_rada = prvni_radek [:3]
    
# zavření souboru - uložený je pouze první řádek a počáteční rok 
    
# definice proměnných 
cislo=0
i=0
vysledky = []
rada = []

# otevření vstupního souboru pro čtení a výstupního souboru pro zápis 
with open ("vstup.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
    
   # výpočet průměru 
    
    for row in reader:
        
        # extrakce roku ze řádku 
        datum_n=(row[2])
        rok_no=(datum_n[-4:])
        rok_n=int(rok_no)
        
        # porovnání roku současného řádku s rokem řádku minulého 
        if rok_n == rok:
            
            # připočtení hodnoty průtoku do proměnné cislo 
            cislo+=float(row[-1])
           
            # aktualizace proměnné rok a proměnné i, která vyjadřuje počet iterací 
            datum=(row[2])
            rok_o=(datum[-4:])
            rok = int(rok_o)
            i=i+1
            
        # v případě, že se hodnota nového roku liší od hodnoty předchozího roku, vezme se součet průtoků z minulého roku
        # a vydělí se počtem iterací (počet dní v daném roce)

        else:
            # výsledek ročního průměru se uloží do seznamu vysledky
            vysledek = cislo/i
            vysledky.append (vysledek)
            
            # do seznamu 'rada' se uloží počáteční řada roku, pro který se bude nyní počítat průměr
            rada.append (row[:3])
            datum=(row[2])
            
            # aktualizace roku
            rok_o=(datum[-4:])
            rok = int(rok_o)

            # vynulování hodnoty proměnných 'i' a 'cislo' a načtení průtoku do proměnné 'cislo'
            cislo = 0
            i=0
            cislo+=float(row[-1])
    
    # vypočtení průměru pro poslední rok a uložení do seznamu 
    i=i+1
    vysledek = cislo/i
    vysledky.append (vysledek)

    # odebrání hodnoty průměrného průtoku prvního roku seznamu 
    prvni_vysledek = vysledky.pop(0)
    # vypsání první řady seznamu a průtoku prvního roku seznamu do souboru 
    outrow=(prvni_rada [0],prvni_rada [1],prvni_rada [2], round (prvni_vysledek,4))
    writer.writerow(outrow)
    
    # vypsání ostatních řad a ročních průtoků do seznamu (dokud budou hodnoty v seznamu vysledky)
    while len(vysledky)>0:
        dalsi_vysledek = vysledky.pop (0)
        dalsi_radek = rada.pop (0)
        outrow=(dalsi_radek[0],dalsi_radek[1],dalsi_radek[2],round (dalsi_vysledek,4))
        writer.writerow(outrow)

