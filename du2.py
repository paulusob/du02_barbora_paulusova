import csv
with open ("vstup_t.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_7dni.csv","w",encoding="utf-8", newline='') as fout,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
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
n=len (a)
#print (n)
m=(n//7)+1
#print (m)
y=7
#cisla=[]

for v in range (m):
    cislo=0
    radek=b.pop (0)
    rada=(radek[0],radek[1],radek[2])
    for z in range (y):
        
        cislo+=float(a.pop (0))
        #cisla.append (cislo)
        #print (a)
        
        #for u in range (6):
            #b.pop(0)
        #print (row)
    
    print (rada, cislo/7)

print (f"Prumerny prutok je: {prutok/len(a)}")


with open ("vstup_t.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_7dni.csv","w",encoding="utf-8", newline='') as fout,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
    
    #prvni_radek=f.readline(4)
    #print (prvni_radek)
    #datum_zac=(prvni_radek[2])
    #rok_zac=(datum_zac[-4:])
    #print(datum_zac)
    #print (rok_zac)

    #extrahovat datum a rok
    
    rok=1980

    a=[]
    b=[]
    i=0
    prutok=0
    cislo=0
    i=1
    for row in reader:
        
        b.append (row)
        datum_n=(row[2])
        rok_n=(datum_n[-4:])
        prutok_den=(row[-1])
        print (rok_n)
        if rok_n == rok:
            a.append(row[-1])
            cislo+=float(a.pop (0))
            datum=(row[2])
            rok(datum[-4:])
            i=i+1
        else:
            vysledek = cislo/i
            print (vysledek)
            print (row[0],row[1],row[2])
            a.clear()
            a.append(row[-1])
            datum=(row[2])
            print (datum)
            #rok(datum[-4:])
            cislo = 0
    
        #rok=(datum[-4:])
        #print(datum)
        #print(rok)

        #try:
            #print(int(row[3]))
        #except ValueError:
            #pass
    #print (b)
    #print (a)
    #print (len (a))
