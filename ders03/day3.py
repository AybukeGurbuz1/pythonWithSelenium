# sınıflar
# modules
# paket yönetimi
# self => this

class Human:
    #name = "Aybüke"  # => Default Value
    #built-in  #constructor  #initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'ı üretildi") # => constructur .. yapıcı blok
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking...")

# instance => örnek
human1 = Human("Ayşe")
human1.talk("Merhaba")
human1.walk()

human2 = Human("Aybüke")
human2.talk("Selam")
human2.walk()
