import csv
import sys

#definice funkcí 

def zapis_vystup (vstupni_radek, vysl_prutok):
    vystup= [vstupni_radek [0],vstupni_radek [1],vstupni_radek [2], "{:.4f}".format(vysl_prutok)]
    writer.writerow(vystup)

def podminky_vstupu (akt_prutok):
    if len(row) != 4:
        print ("Vstup není v požadovaném formátu, program očekává data ve 4 sloupcích:\
        databázové číslo, označení typu dat, datum, průměrný denní průtok")
        print (f, "K chybě došlo na řádku {row}")
        sys.exit()
    try:
        akt_prutok=float(row[-1])
    except ValueError:
        print (f, "Průtok na řádku {row} není číselná hodnota, zkontrolujte hodnoty průtoku ve čtvrtém sloupci")
        sys.exit ()
    return akt_prutok
    
def extr_rok (f_row):
    try:
        datum_f=f_row[2]
        vystup_rok=int(datum_f.split('.')[2])
    except ValueError:
         print (f, "Rok na řádku {row} není číselná hodnota, zkontrolujte datum")
         sys.exit()
    return vystup_rok


# výpočet sedmidenního průtoku
# načtení souboru a uložení potřebných údajů do seznamů 

# otevření souboru pro čtení, ošetření nenalezení souboru
try:
    with open ("vstup.csv", encoding="utf-8", newline='') as f: #,\
        
        reader=csv.reader(f, delimiter=",")
        
        # vytvoření prázdných seznamů 'a' a 'b', definice proměnné průtok
        prutoky=[]
        radky=[]
        prutok=0

        # uložení řádky a průtoku do proměnné a ověření korektnosti vstupu - 
        # v případě jiného počtu sloupců a nepřítomnosti čéselné hodnoty průtoku se program ukončí 
        for row in reader:
            podminky_vstupu(prutok)
                
            prutoky.append(row[-1])
            radky.append(row)
except FileNotFoundError:
    print ('Vstupní soubor nebyl nalezen, zkontrolujte název a umístění souboru')
    sys.exit()


# definice 'n' (počet hodnot průtoků v seznamu) a 'y' (definice počtu iterací)
n=int(len(prutoky))
delka_bloku=7 

# otevření souboru pro zápis 

with open ("vystup_7dni.csv","w",encoding="utf-8", newline='') as fout:
    writer = csv.writer (fout)
    
    # dokud je počet prvků v seznamu 7 a více, provádí se výpočet sedmidenního průměru průtoku 
    while n >=delka_bloku:
        kumul_prutok=0

        # extrakce prvního dne ze sedmi dnů, pro které je počítán průměr
        radek=radky.pop (0)

        
        # načítání jednotlivých průtoků do proměnné kumul_prutok (kumulativní průtok)
        for z in range (delka_bloku):
            kumul_prutok+=float(prutoky.pop(0))
                
        # odebrání nepotřebných řádků 
        for u in range (delka_bloku-1):
            radky.pop (0)
        
        # vypsání výsledku do souboru 
        vysledek=kumul_prutok/delka_bloku
        zapis_vystup (radek,vysledek)
        
        n=int(len (prutoky))
    
    # pokud je počet hodnot průtoku v seznamu menší než 7, počítá se průměr z těchto zbylých hodnot 
    
    # extrakce prvního dne 
    if len(radky)>0:
        radek = radky.pop (0)

    # definice proměnné i, která udává počet provedených iterací 
        i=0
        kumul_prutok=0

    # dokud není seznam prázdný, budou se průtoky připočítávat do proměnné kumul_prutok, následně se vydělí počtem hodnot (počet iterací)
        while n>0:
            kumul_prutok+=float(prutoky.pop (0))
            n=int(len (prutoky))
            i=i+1

            
    # průměrný průtok posledních dní se vypočítá v proměnné outrow a zapíše se do souboru 
        vysledek=kumul_prutok/i
        zapis_vystup (radek,vysledek)
    
print ("Výsledné sedmidenní průtoky jsou uloženy v souboru vystup_7dni.csv")    


# výpočet průměrného ročního průtoku 

# otevření souboru s daty pro čtení, ošetření nenalezení souboru
try:
    with open ("vstup.csv", encoding="utf-8", newline='') as f:
        reader=csv.reader(f, delimiter=",")
        
        # vytvoření seznamů pro uložení roků a řádků
        roky=[]
        radky=[]

        # Ověření korektnosti vstupu, vyextrahování řádků a roků a načtení do seznamů radky a roky
        for row in reader: 
            podminky_vstupu (prutok)

            radek=(row)
            radky.append (radek) 

            datum_m=(row[2])
            roky.append (int(datum_m[-4:]))
            
        
        
except FileNotFoundError:
    print ('Vstupní soubor nebyl nalezen, zkontrolujte název a umístění souboru')
    sys.exit()
# zavření souboru - uložený je pouze první řádek a počáteční rok 

# odebrání prvního řádku a uložení prvních tří atributů do proměnné prvni rada
prvni_radek=[]
prvni_radek = radky.pop(0)
prvni_rada = prvni_radek [:3] 
# odebrání prvního roku a převedení do proměnné rok 
prvni_rok = roky.pop(0)
rok=prvni_rok

# definice proměnných 
kumul_prutok=0
i=1
vysledky = []
radky = []

# otevření vstupního souboru pro čtení a výstupního souboru pro zápis 
with open ("vstup.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
    
   # výpočet průměru 
    
    for row in reader:

        rok_n = extr_rok(row)
                
        # porovnání roku současného řádku s rokem řádku minulého 
        if rok_n == rok:
            
            # připočtení hodnoty průtoku 
            kumul_prutok+=float(row[-1])
           
            # aktualizace proměnné rok a proměnné i, která vyjadřuje počet iterací 
            rok = extr_rok(row)
            i=i+1
            
        # v případě, že se hodnota nového roku liší od hodnoty předchozího roku, vezme se součet průtoků z minulého roku
        # a vydělí se počtem iterací (počet dní v daném roce)

        else:
            # výsledek ročního průměru se uloží do seznamu vysledky
            vysledek = kumul_prutok/i
            vysledky.append (vysledek)
            
            # do seznamu 'rada' se uloží počáteční řada roku, pro který se bude nyní počítat průměr
            radky.append (row)
            datum=(row[2])
            
            # aktualizace roku
            rok_o=(datum[-4:])
            rok = int(rok_o)

            # vynulování hodnoty proměnných 'i' a 'cislo' a načtení průtoku do proměnné 'cislo'
            kumul_prutok = 0
            i=1
            kumul_prutok+=float(row[-1])
    
    # vypočtení průměru pro poslední rok a uložení do seznamu 
    i=i+1
    vysledek = kumul_prutok/i
    vysledky.append (vysledek)

    # vypisování výsledků do výstupního souboru

    # odebrání hodnoty průměrného průtoku prvního roku seznamu 
    prvni_vysledek = vysledky.pop(0)
    # vypsání první řady seznamu a průtoku prvního roku seznamu do souboru 
    zapis_vystup(prvni_rada,prvni_vysledek)
    
    # vypsání ostatních řad a ročních průtoků do souboru (dokud budou hodnoty v seznamu vysledky)
    while len(vysledky)>0:
        dalsi_vysledek = vysledky.pop (0)
        dalsi_radek = radky.pop (0)
        zapis_vystup(dalsi_radek,dalsi_vysledek)
print ("Výsledné roční průtoky jsou uloženy v souboru vystup_rok.csv") 