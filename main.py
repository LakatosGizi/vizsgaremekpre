# adatok beolvasása listába 1.
adatok=[]
with open("data.txt" , "r" , encoding="utf-8") as fin:
    for sor in fin:
        adatok.append(int(sor))
print(adatok)
# adatok átlaga 2.
atlag=sum(adatok)/len(adatok)
print(f"a beolvasott adatok átlaga: {atlag: .2f}")
# döntsűk el hogy volt e négyes 3.
van=False
for szam in adatok:
    if szam==4:
        van = True
        break
if van:
    print("vam négyes.")
else:
    print("nincs négyes")
# keresűk meg hogy volt e ötös 4.
van5 = False
for i in range(len(adatok)):
    if adatok[i]==5:
        van5=True
        break
if van5:
    print(f"van ötös, és a(z) {i}. elem.")
else:
    print("nincs ötös.")
# hány darab kilences volt 5.
db=0
for szam in adatok:
    if szam == 9:
        db += 1
print(f"{db}darab kilences szám van.")
# mennyi a legnagyobb beirt szám 6.
legnagyobb_szam=adatok[0]
for szam in adatok:
    if szam>legnagyobb_szam:
        legnagyobb_szam = szam
print(f"legnagyobb szám {legnagyobb_szam}")
# hanyadik indexen van a legkisebb elem 7.
minindex=0
for i in range(len(adatok)):
    if adatok[i]< minindex:
        minindex=i
print(f"a legkiseb elem a(z) {minindex} és a(z). elem.")
# ird ki a páros számokat a paros.txt be 8.
with open ("paros.txt","w") as fout:
    for szam in adatok:
        if szam % 2==0:
            print(szam, file=fout)