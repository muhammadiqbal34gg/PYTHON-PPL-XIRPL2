#kelas induk = kendaraan  kelas turunan = mobil
#kendaraan mempunyai sifat berjalan(), Mobil Mempnyai sifat berjalan() tapi lebih spesifik

class kendaraan:
    def berjalan(self):
        print('Berjalan')

class mobil(kendaraan):
    def berjalan(self, kecepatan, satuan = 'km/j'):
        print(f'Berjalan lebih ngebut {kecepatan} {satuan}')

sepeda = kendaraan()
sedan = mobil()

sepeda.berjalan()
sedan.berjalan(200)