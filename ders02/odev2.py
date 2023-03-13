                                                     #******ödev2******#
# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

### Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
ogrenciler = ["Aybüke Gürbüz", "Ali Kamil Gürbüz", "Ceyda Gürbüz"]
print(ogrenciler)

### Aldığı isim soy isim ile listeye öğrenci ekleyen fonksiyon
ogrenciler.append("Necip Gürbüz")
print(ogrenciler)

### Aldığı isim soy isim ile eşleşen değeri listeden kaldıran fonksiyon
ogrenciler.remove("Aybüke Gürbüz")
print(ogrenciler)

#### Listeye birden fazla öğrenci eklemeyi mümkün kılan fonksiyon
ogrenciler.extend(["Ayşenur Gürbüz", "Yunus Gürbüz"])
print(ogrenciler)

### Listedeki tüm öğrencileri tek tek ekrana yazdıran fonksiyon
for tümOgrenciler in ogrenciler:
    print(tümOgrenciler)

### Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan fonksiyon
ogrenciAdı= input("Öğrencinin adını girin: ")  # öğrencinin adını kullanıcıdan alıyoruz

if ogrenciAdı in ogrenciler:  # öğrenci listede varsa
    ogrenciNo = ogrenciler.index(ogrenciAdı) + 1  # öğrencinin numarasını hesaplıyoruz
    print(f"{ogrenciAdı} öğrencisi, {ogrenciNo}. sırada yer almaktadır.")
else:
    print(f"{ogrenciAdı} öğrencisi listede bulunamadı.")    

### Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız) fonksiyon
silinecekOgrenciler = ["Necip Gürbüz","Ayşenur Gürbüz"]

def ogrenciSil(ogrenciler, silinecekOgrenciler):
    i = 0
    while i < len(silinecekOgrenciler):
        if silinecekOgrenciler[i] in ogrenciler:
            ogrenciler.remove(silinecekOgrenciler[i])
        i += 1
    return ogrenciler










