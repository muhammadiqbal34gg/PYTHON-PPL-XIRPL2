class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
    
    def perkenalan(self):
        print("Perkenalkan nama saya", self.nama,"dari",self.asal)

class Pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah = sekolah

class Pekerja(Orang):
     def __init__(self, nama, asal, kerja):
        Orang.__init__(self, nama, asal)
        self.kerja = kerja

dani = Orang('Dani','Solo')
dani.perkenalan()

rahma = Pelajar('rahma','jawa','SMK JP 1')
rahma.perkenalan()
print("Saya bersekolah di", rahma.sekolah , "/n")

kakarya = Pekerja('kakarya','pakistan')
kakarya.perkenalan()
print("Saya bekerja di", kakarya.kerja, "/n")