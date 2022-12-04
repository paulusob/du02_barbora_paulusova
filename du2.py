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
        print(n)
    radek = b.pop (0)
    rada=(radek[0],radek[1],radek[2])
    print (rada)
    i=0
    while n>0:
        try:
            cislo=0
            cislo+=float(a.pop (0))
            #print (rada, cislo/7)
            #print(b)
            #radek=b.pop (0)
            n=int(len (a))
            print(n)
            i=i+1
        except ValueError:
            continue

    outrow = [rada,cislo/i]
    print (outrow)
    writer.writerow(outrow)
    
    print (n)

