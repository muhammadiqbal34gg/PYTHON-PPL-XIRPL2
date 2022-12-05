# ada 3 kategori enkalupsi yaitu : Public, Protected, Private

#Contoh Class public
class segitiga:
    def __init__(self , alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

#buat instansiasinya
segitiga_besar = segitiga(100,80)

print(f'alas : {segitiga_besar.alas}')
print(f'tinggi : {segitiga_besar.tinggi}') 
print(f'luas : {segitiga_besar.luas}')

class cool:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = posisi
    
barudak = cool('Alisson','GK')

print(f'Kiper Liverpool bernama {barudak.nama} dengan posisi {barudak.posisi}')

#Contoh Class Protected
class mobil:
    def __init__(self, merk):
        self._merk = merk

class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)  
        self._total_gear = total_gear

    #Akses _merk dari subclass (kelas turunan)
    def pamer(self):
        print(f'Mobil{self._merk} dengan total gear {self._total_gear}') 

#Class si paling sulid di akses (Private)
class motor:
    def __init__(self, merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print(f'Merk motornya : {self.__merk}')

ducati = motor('Ducati')
ducati.tampilkan_merk()

# sedan = mobil('Toyota')

# tampilkan merk dari luar kelas
# print (f'Merk Mobil : {sedan._merk}')
