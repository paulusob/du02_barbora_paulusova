import csv
with open ("vstup.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
    

    rok_m=[]
    radek_m=[]

    for row in reader: 
        radek=(row[:3])
        radek_m.append (radek) 
        datum_m=(row[2])
        rok_m.append (int(datum_m[-4:]))
        
    prvni_rok = rok_m.pop(0)
    rok=int(prvni_rok)
    print (rok)
    prvni_radek=[]
    prvni_radek = radek_m.pop(0)
    
    prvni_rada = prvni_radek [:3]
    print(prvni_rada)


    a=[] #vytvoření prázdného seznamu 
    
    
cislo=0
i=0
vysledky = []
rada = []
print (cislo)


with open ("vstup.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
    
   
    writer.writerow(prvni_rada)
    
    for row in reader:
        
        datum_n=(row[2])
        rok_no=(datum_n[-4:])
        rok_n=int(rok_no)
        

        
        if rok_n == rok:
            
            cislo+=float(row[-1])
           
            datum=(row[2])
            rok_o=(datum[-4:])
            rok = int(rok_o)
            i=i+1
            
        else:
            
            vysledek = cislo/i
            
            
            vysledky.append (vysledek)
            
            
            
            rada.append (row[:3])
            print (rada)
            datum=(row[2])
            
            rok_o=(datum[-4:])
            rok = int(rok_o)
            cislo = 0
            i=0
            cislo+=float(row[-1])
    
    i=i+1
    vysledek = cislo/i
    
    vysledky.append (vysledek)
    prvni_vysledek = vysledky.pop(0)
    print (prvni_vysledek)
    outrow=(prvni_rada, prvni_vysledek)
    writer.writerow(outrow)
    print (vysledky)
    print (len(vysledky))
    while len(vysledky)>0:
        dalsi_vysledek = vysledky.pop (0)
        dalsi_radek = rada.pop (0)
        outrow=(dalsi_radek,dalsi_vysledek)
        writer.writerow(outrow)
    
