import csv
with open ("vstup_t.csv", encoding="utf-8", newline='') as f,\
    open ("vystup_7dni.csv","w",encoding="utf-8", newline='') as fout,\
    open ("vystup_rok.csv","w",encoding="utf-8", newline='') as fout:
    reader=csv.reader(f, delimiter=",")
    writer = csv.writer (fout)
    a=[]
    prutok=0
    for row in reader:
        a.append(row[-1])

        #print(row)
        #print(row[-1])
        try:
            prutok+= float(row[-1])
            print(int(row[3]))
        except ValueError:
            pass
#print (a)
#print (len (a))
n=len (a)
print (n)
m=(n//7)+1
print (m)
y=7
#cisla=[]

for v in range (m):
    cislo=0
    for z in range (y):
        cislo+=float(a.pop (0))
        #cisla.append (cislo)
        #print (a)
    print (cislo/7)


print (f"Prumerny prutok je: {prutok/len(a)}")

