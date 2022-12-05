import csv

#sedmidenní průměr
with open ("vstup_t.csv", encoding="utf-8", newline='') as f: #,\
    #open ("vystup_7dni.csv","w",encoding="utf-8", newline='') as fout: #,\
    #open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    reader=csv.reader(f, delimiter=",")
    #writer = csv.writer (fout)
    a=[]
    b=[]
    prutok=0
    for row in reader:
        a.append(row[-1])
        b.append (row)
        #print(row)
        #print(row[-1])
        try:
            prutok+= float(row[-1])
            #print(int(row[3]))
        except ValueError:
            pass
    #print (b)
    #print (a)
    #print (len (a))
n=int(len (a))
#print (n)
#m=(n//7)
#print (m)
y=7
#print (a,b)
#cisla=[]
#try: 
#for v in range (m):

with open ("vystup_7dni.csv","w",encoding="utf-8", newline='') as fout:
    writer = csv.writer (fout)
    #print (n)
    while n >=y:
        cislo=0
        radek=b.pop (0)
        rada=(radek[0],radek[1],radek[2])
        #print (n)
        for z in range (y):
            
            cislo+=float(a.pop(0))
            #radek=b.pop (0)
            #cisla.append (cislo)
            #print (a)
            
            #for u in range (6):
                #b.pop(0)
            #print (row)
        for u in range (6):
            radek=b.pop (0)
        #print (rada, cislo/7)
        outrow = [rada,cislo/7]
        writer.writerow(outrow)
        n=int(len (a))
        #print(n)
    radek = b.pop (0)
    rada=(radek[0],radek[1],radek[2])
    #print (rada)
    i=0
    cislo=0
    while n>0:
        try:
            cislo+=float(a.pop (0))
            #print (rada, cislo/7)
            #print(b)
            #radek=b.pop (0)
            n=int(len (a))
            #print(n)
            i=i+1
            #print(i)
            #print (cislo)
        except ValueError:
            continue

    outrow = [rada,cislo/i]
    #print (outrow)
    writer.writerow(outrow)
    
    #print (n)

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
    #print (rok)
    prvni_radek=[]
    prvni_radek = radek_m.pop(0)
    
    prvni_rada = prvni_radek [:3]
    #print(prvni_rada)


    a=[] #vytvoření prázdného seznamu 
    
    
cislo=0
i=0
vysledky = []
rada = []
#print (cislo)


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
            #print (rada)
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
    #print (prvni_vysledek)
    outrow=(prvni_rada, prvni_vysledek)
    writer.writerow(outrow)
    #print (vysledky)
    #print (len(vysledky))
    while len(vysledky)>0:
        dalsi_vysledek = vysledky.pop (0)
        dalsi_radek = rada.pop (0)
        outrow=(dalsi_radek,dalsi_vysledek)
        writer.writerow(outrow)
    
