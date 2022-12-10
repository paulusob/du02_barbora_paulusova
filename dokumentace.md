# Vývojářská dokumentace - Program pro výpočet průměrných sedmidenních a ročních průtoků
Program načítá historická data o průměrných denních průtocích a vypočítává průměrné sedmidenní a roční průměry. Program je rozdělen na dvě části - v první části programu je počítán sedmidenní průměr, v druhé části souboru průměr roční.

## Funkce
V úvodu programu jsou definovány funkce, které jsou následně používány. Funkce jsou blíže popsány níže.

## Výpočet průměrného sedmidenního průtoku 

**Načtení souboru**\
Pomocí příkazu *with open* program načte vstupní soubor dat *vstup.csv*, který by měl být ve formátu csv a v jednotlivých řádcích by měl obsahovat *databázové číslo, označení typu dat, datum, průměrný denní průtok* pro každý měřený den. 

**Vytvoření seznamů**\
Nejprve se vytvoří prázdné seznamy *prutoky* a *radky*, do kterých budou následně přiřazovány hodnoty z jednotlivých řádků.

**Ověření vstupu**\
Nejdříve je ověřováno, zda je možné soubor otevřít, tedy že má předpokládaný název a je umístěn ve stejné složce. Pomocí funkce *podminky_vstupu* se následně ověří, zda má vstupní soubor požadovaný formát, tedy že má 4 sloupce a v posledním sloupci se nachází číselná hodnota průměrného denního průtoku. Pokud není vstupní soubor nalezen pod názvem *vstup.csv*, program upozorní uživatele a skončí, stejně jako v případě, že uživatel nemá přístupová práva k vstupnímu souboru.

**Výpočet průměru**\
Následně se pomocí příkazu *with open* otevře soubor pro zápis spočtených výsledků 'vystup_7dni.csv'.
Z již vytvořeného seznamu *prutoky* se postupně odebírají hodnoty průtoků a přiřazují se do proměnné *cislo*. Tato operace se opakuje pro 7 řádků a následně je tento cyklus přerušen a vypisuje se průměr součtu průtoků s odpovídajícím dnem ze seznamu *radky*. Následně se odebere
6 řádků, které nejsou potřeba, vynuluje se proměnná *cislo* a stejným způsobem se počítá průměrný průtok pro následujících 7 dní.
Výsledky zaokrouhlená na 4 desetinná místa jsou s odpovídajícími počátečními dny zapsány do souboru *vystup_7dni* pomocí funkce *zapis_vystup*, která je definována na začátku souboru. 
Tato iterace končí, pokud je v seznamu průtoků méně než 7 prvků. V tomto případě se pomocí funkce *zapis_vystup* vypisuje následující den (pokud ještě nějaký zbývá) a stejným způsobem se přičítají hodnoty průtoku do proměnné *cislo*. Součet hodnot průtoků je následně vydělen počtem iterací a výsledek 
je s odpovídajícím dnem taktéž zapsán do souboru *vystup_7dni*.

## Výpočet průměrného ročního průtoku 

**Vytvoření seznamů**\
Nejprve se vytvoří prádné seznamy *vysledky* a *radky*, do kterých budou následně přiřazovány roční výsledky a první řádky roků, pro které je počítán průměr. 

**Načtení souboru**\
Pomocí příkazu *with open* program načte vstupní soubor dat *vstup.csv*, pro který platí stejné parametry pro ověření jako u výpočtu sedmidenního průtoku.

**Extrakce první řady souboru**\
Program přečte první řádek a uloží ho do seznamu *radky*. Pomocí funkce *extr_rok* se extrahuje první rok souboru a uloží se do proměnné *rok*. Průtok prvního dne souboru se načte do proměnné *kumul_prutok*.

**Výpočet průměru**\
Pro každý řádek se pomocí funkce *extr_rok* extrahuje rok, který se následně porovnává s rokem řádku předchozího, respektive počátečního.
V případě, že je rok daného řádku stejný jako rok řádku předchozího, průtok každého řádku se připočítává do proměnné *cislo*.
V případě změny roku se součet průtoků předchozích řádků vydělí počtem provedených iterací a výsledek se zapíše do seznamu *vysledky*. 
Do seznamu *rada* se uloží první řádek s jinou hodnotou roku - tedy první den dalšího roku, pro který se bude počítat roční průměr. 
Tento proces se opakuje a v posledním kroku je do seznamu zapsán i průměrný průtok posledního roku (mimo cyklus).

**Výpis výsledků**\
Jednotlivé počáteční řádky i výsledky se postupně odebírají ze seznamů *radky* a *vysledky* a pomocí funkce *zapis_vystup* se vypisují do výstupního souboru *vystup_rok*. 

