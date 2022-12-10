# du02_barbora_paulusova
# Program pro výpočet průměrných sedmidenních a ročních průtoků
Program načítá historická data o průměrných denních průtocích a vypočítává průměrné sedmidenní a roční průměry. Program je rozdělen na dvě části - v první části programu je počítán sedmidenní průměr, v druhé části souboru průměr roční. 

## Vstup 
Program načítá CSV soubor s názvem **vstup.csv**, který obsahuje průměrné denní průtoky vodního toku. Vstupní soubor musí být strukturován do čtyř sloupců ve kterých je zapsáno  *databázové číslo, označení typu dat, datum a průměrný denní průtok*. Jednotlivé sloupce jsou oddělovány čárkami. 

## Výstupy
Program vytváří samostatné soubory *vystup_7dni* a *vystup_rok*, do kterých se zapisují výsledné hodnoty sedmidenních a ročních průtoků. V každém souboru je vždy vypsán řádek prvního dne, pro který se počítá průměrný sedmidenní respektive roční průtok. 
