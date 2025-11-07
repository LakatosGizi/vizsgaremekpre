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

# keresűk meg hogy volt e ötös 4.
with open("jegyek.txt", "r", encoding="utf-8") as fin:
    jegyek =()

if 5 in jegyek:
    print("Volt ötös!")
else:
    print("Nem volt ötös.")
# hány darab kilences volt 5.

# mennyi a legnagyobb beirt szám 6.

# hanyadik indexen van a legkisebb elem 7.

# ird ki a páros számokat a paros.txt be 8.