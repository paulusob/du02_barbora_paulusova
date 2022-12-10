import csv
import sys

# definice funkcí 

def zapis_vystup (vstupni_radek, vysl_prutok):
    vystup= [vstupni_radek [0],vstupni_radek [1],vstupni_radek [2], "{:.4f}".format(vysl_prutok)]
    writer.writerow(vystup)

def podminky_vstupu (f_row):
    if len(f_row) != 4:
        print ("Vstup není v požadovaném formátu, program očekává data ve 4 sloupcích:\
        databázové číslo, označení typu dat, datum, průměrný denní průtok")
        print (f, "K chybě došlo na řádku {f_row}")
        sys.exit()
    try:
        akt_prutok=float(f_row[-1])
    except ValueError:
        print (f, "Průtok na řádku {f_row} není číselná hodnota, zkontrolujte hodnoty průtoku ve čtvrtém sloupci")
        sys.exit ()
    return akt_prutok
    
def extr_rok (f_row):
    try:
        datum_f=f_row[2]
        vystup_rok=int(datum_f.split('.')[2])
    except ValueError:
         print (f, "Rok na řádku {f_row} není číselná hodnota, zkontrolujte datum")
         sys.exit()
    return vystup_rok


# výpočet sedmidenního průtoku 

# otevření souboru pro čtení, ošetření nenalezení souboru a přístupových práv 
try:
    with open ("vstup.csv", encoding="utf-8", newline='') as f: #,\
        
        reader=csv.reader(f, delimiter=",")
        
        # vytvoření prázdných seznamů pro ukládání průtoků a řádků, definice proměnné průtok
        prutoky=[]
        radky=[]
        prutok=0

        # uložení řádky a průtoku do seznamu průtoků a řádků a ověření korektnosti vstupu - 
        # v případě jiného počtu sloupců a nepřítomnosti číselné hodnoty průtoku se program ukončí 
        for row in reader:
    
            prutoky.append(podminky_vstupu(row))
            
            radky.append(row)
            
except FileNotFoundError:
    print ('Vstupní soubor nebyl nalezen, zkontrolujte název a umístění souboru')
    sys.exit()
except PermissionError:
    print ('K otevření souboru nejsou přístupová práva')
    sys.exit()


# definice 'n' (počet hodnot průtoků v seznamu) a délky bloku (počet iterací)
n=int(len(prutoky))
delka_bloku=7 

# otevření souboru pro zápis, ošetření přístupových práv
try:
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

except PermissionError:
    print ('K vytvoření souboru nejsou přístupová práva')
    sys.exit()
print ("Výsledné sedmidenní průtoky jsou uloženy v souboru vystup_7dni.csv")    


# výpočet průměrného ročního průtoku 

# vytvoření seznamů, do kterých se budou ukládat jednotlivé řádky a roční průměry (vysledky)
radky=[]
vysledky = []

# definice proměnných 
kumul_prutok=0
i=1

# otevření vstupního souboru pro čtení a výstupního souboru pro zápis, ošetření nenalezení souboru, povolení otevření a zápisu do souboru a 
try:
    with open ("vstup.csv", encoding="utf-8", newline='') as f,\
        open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
        
        reader=csv.reader(f, delimiter=",")
        writer = csv.writer (fout)

        # extrakce první řady souboru 
        prvni_rada=[]
        prvni_rada=f.readline()
        prvni_rada=prvni_rada.split(',')

        # extrakce prvního roku souboru, uložení prvního řádku do seznamu rádků, načtení průtoku prvního dne do proměnné kumul_prutok
        rok=extr_rok(prvni_rada)
        radky.append(prvni_rada)
        kumul_prutok=float(podminky_vstupu(prvni_rada))
        i=1
        
        # výpočet průměru 
        
        for row in reader:
            
            # extrakce nového roku ze řádku
            rok_n = extr_rok(row)
            
            # porovnání roku současného řádku s rokem řádku minulého 
            if rok_n == rok:
                
                # připočtení hodnoty průtoku (kumulativní průtok za daný rok)
                kumul_prutok+=float(podminky_vstupu(row))
                
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
                rok = extr_rok(row)

                # vynulování hodnoty proměnných 'i' a 'cislo' a načtení průtoku do proměnné 'cislo'
                kumul_prutok = 0
                i=1
                kumul_prutok+=float(podminky_vstupu(row))
        
        # vypočtení průměru pro poslední rok a uložení do seznamu 
        i=i+1
        vysledek = kumul_prutok/i
        vysledky.append (vysledek)

        # vypisování výsledků do výstupního souboru

        # vypsání řádků a ročních průtoků do souboru (dokud budou hodnoty v seznamu vysledky)
        while len(vysledky)>0:
            rocni_prumer = vysledky.pop (0)
            radek_prumeru = radky.pop (0)
            zapis_vystup(radek_prumeru,rocni_prumer)
except FileNotFoundError:
    print ('Vstupní soubor nebyl nalezen, zkontrolujte název a umístění souboru')
    sys.exit()
except PermissionError:
    print ('K otevření souboru nejsou přístupová práva')
    sys.exit()

print ("Výsledné roční průtoky jsou uloženy v souboru vystup_rok.csv") 