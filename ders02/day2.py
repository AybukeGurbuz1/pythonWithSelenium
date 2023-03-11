faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi)) --> ValueError: invalid literal for int() with base 10: 'İhtiyaç Kredisi'
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayisini giriniz: "))
print(type(vade))
vade = vade + 12

# string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Aybüke"
metin = "Merhaba {name}".format(name=isim)
print(metin)

# f-string
metin = f"Hoşgeldiniz {isim}"
print(metin)

# Listeler

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0]) 

print(len(krediler)) #length
# print(krediler[3]) => hata verir

krediler.append("Özel kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# Döngüler
# for
# i=0 i<10 

for i in range(10):
    print("xx")
    print(i)
print("********************")

for i in range(5,10):
    print(i)
print("********************")

for i in range(0,51,10):
    print(i)
print("********************")

#for i in range(0.1,0.5):
#    print(i)
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("********************")

for i in range(len(krediler)):
    print(krediler[i])
print("********************")

#while
#sonsuz döngü --> konsol ctrl+C ile durdurulabilir
i = 0
while i<10:
    print("x")
    i += 1
print("y")

print("********************")

while True:
    print("X")
    break

print("*****son döngü*********")

i = 0
while i < len(krediler):
    print(i)
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break

# Fonksiyonlar

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim) 

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Aybüke")
sayHello("Ceyda")

def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

#void
def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("********************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"151.satır: {fonk1+100}")
print(f"152.satır: {fonk2+100}")
print("********************")










    













