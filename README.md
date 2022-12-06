# du02_barbora_paulusova
# Program pro výpočet průměrných sedmidenních a ročních průtoků
Program slouží k výpočtu sedmidenního a ročního průtoku z denních dat. Je rozdělen na dvě části - v prní části se počítá průměrný sedmidenní průtok, v druhé části potom průměrný roční průtok. Postupy jsou analogické, ale pro větší přehlednost jsou uvedeny samostatně.  

## Výpočet průměrného sedmidenního průtoku 

**Načtení souboru**
Pomocí příkazu *with open* program načte vstupní soubor dat *vstup.csv*, který by měl být ve formátu csv a v jednotlivých řádcích by měl obsahovat *databázové číslo, označení typu dat, datum, průměrný denní průtok* pro každý měřený den. 

**Vytvoření seznamů**
Nejprve se vytvoří prázdné seznamy *prutoky* a *radky*, do kterých budou následně přiřazovány hodnoty z jednotlivých řádků.

**Ověření vstupu**
V dalším bloku se pomocí funkce ověří, zda má vstupní soubor požadovaný formát, tedy že má 4 sloupce a v posledním sloupci se nachází číselná hodnota průměrného denního průtoku. 

**Výpočet průměru**
Následně se pomocí příkazu *with open* otevře soubor pro zápis spočtených výsledků 'vystup_7dni.csv'.
Z již vytvořeného seznamu *prutoky* se postupně odebírají hodnoty průtoků a přiřazují se do proměnné *cislo*. Tato operace se opakuje pro 7 řádků a následně je tento cyklus přerušen a vypisuje se průměr součtu průtoků s odpovídajícím dnem ze seznamu *radky*. Následně se odebere
6 řádků, které nejsou potřeba, vynuluje se proměnná *cislo* a stejným způsobem se počítá průměrný průtok pro následujících 7 dní.
Výsledky zaokrouhlená na 4 desetinná místa jsou s odpovídajícími počátečními dny zapsány do souboru *vystup_7dni*. 
Tato iterace končí, pokud je v seznamu průtoků méně než 7 prvků. V tomto případě se vypisuje následující den (pokud ještě nějaký zbývá) a stejným způsobem se přičítají hodnoty průtoku do proměnné *cislo*. Součet hodnot průtoků je následně vydělen počtem iterací a výsledek 
je s odpovídajícím dnem taktéž zapsán do souboru *vystup_7dni*.

## Výpočet průměrného ročního průtoku 

**Načtení souboru**
Pomocí příkazu *with open* program načte vstupní soubor dat *vstup.csv*, pro který platí stejné parametry jako u výpočtu sedmidenního průtoku.

**Vytvoření seznamů**
Nejprve se vytvoří prádné seznamy *roky* a *radky*, do kterých budou následně přiřazovány hodnoty z jednotlivých řádků.

**Ověření vstupu**
V dalším bloku se pomocí funkce ověří, zda má vstupní soubor předpokládaný formát, tedy že má 4 sloupce a v posledním sloupci se nachází číselná hodnota průměrného denního průtoku. Do seznamu *roky* se přiřadí roky z jednotlivých řádků, do seznamu *radky* jednotlivé řádky.

**Extrakce parametrů z prvního řádku**
Následně se ze seznamů odebere první řádek souboru, který se uloží pro pozdější zápis prvního výsledku. Taktéž se vyextrahuje první rok ze seznamu, se kterým se v dalším kroku porovnává rok dalšího řádku. 

**Výpočet průměru**
Definují se proměnné a seznamy, do kterých se ukládají dílčí výsledky a následně se znovu otevře soubor *vstup.csv* pro čtení a soubor *vystup_rok* pro zápis. Pro každý řádek se extrahuje rok, který se následně porovnává s rokem řádku předchozího, respektive počátečního.
V případě, že je rok daného řádku stejný jako rok řádku předchozího, se průtok každého řádku připočítává do proměnné *cislo*.
V případě změny roku se součet průtoků předchozích řádků vydělí počtem provedených iterací a výsledek se zapíše do seznamu *vysledky*. 
Do seznamu *rada* se uloží první řádek s jinou hodnotou roku - tedy první den dalšího roku, pro který se bude počítat roční průměr. 
Tento proces se opakuje a v posledním kroku je do seznamu zapsán i průměrný průtok posledního roku (mimo cyklus).

**Výpis výsledků**
Jednotlivé počáteční řádky i výsledky se postupně odebírají ze seznamů *rada* a *vysledky* a ukládají se do výstupního souboru vystup_rok. 
Pro první rok je tato operace provedena samostatně, neboť se první řádek nevypisuje v cyklu. 


