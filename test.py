import csv
with open ("vstup.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
    
    #prvni_radek=f.readline()
    #print (prvni_radek)

    rada=[]
    rada = f.readline()
    print(rada)

    #datum_zac=(prvni_radek[2])
    #rok_zac=(datum_zac[-4:])
    #print(datum_zac)
    #print (rok_zac)

    rok=int(rada.split(',')[2][-4:])
    prvni_rok = (rada.split(',')[:3])
    #print(prvni_rok)
    #print(rok)

    #writer.writerow(prvni_rok)


     #nastavení počátečního roku - vyextrahovat z prvního řádku

    a=[] #vytvoření prázdného seznamu 
    
    
    cislo=0
    i=0


    for row in reader:
        #print(row)
        datum_n=(row[2])
        rok_no=(datum_n[-4:])
        rok_n=int(rok_no)
        #prutok_den=(row[-1])
        #print (rok_n)
        if rok_n == rok:
            #a.append(row[-1])
            cislo+=float(row[-1])
            #(a.pop (0))
            datum=(row[2])
            rok_o=(datum[-4:])
            rok = int(rok_o)
            i=i+1
            #print (i)
        else:
            #print(cislo)
            #print(a)
            vysledek = cislo/i
            outrow = [rada,vysledek]
            #print(vysledek)
            #print(outrow)
            #print (f"{rada} {vysledek} \n ")
            writer.writerow(outrow)
            rada = row[:3]
            #print (row[0],row[1],row[2])
            #a.clear()
            #a.append(row[-1])
            datum=(row[2])
            #print (datum)
            rok_o=(datum[-4:])
            rok = int(rok_o)
            cislo = 0
            i=0
            cislo+=float(row[-1])
    
    vysledek = cislo/i
    outrow = [rada,vysledek]
    writer.writerow(outrow)
    #print (f"{rada} {vysledek} \n ")
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