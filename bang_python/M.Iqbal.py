#Public
#Siswa kami bernama Dava
class empring:
    def __init__(self, siswa):
        self.siswa = siswa

empring_gg = empring('Dava')

print(f'Siswa Kami bernama {empring_gg.siswa}')

#Protected
#Guru Dava bernama Arya 
class suhu:
    def __init__(self, murid):
        self._murid = murid

class sensei(suhu):
    def __init__(self, murid, guru):
        super().__init__(murid)
        self._guru = guru
    
    def gg(self):
        print(f'Guru {self._murid} bernama {self._guru}')
asem = sensei('Dava', 'Arya')
asem.gg()

#Private
#Kepsek Arya bernama pak Lilik
class kepsek:
    def __init__(self, nama):
        self.__nama = nama

    def pak_kepsek(self):
        print(f'Kepsek Arya bernama {self.__nama}')

pak = kepsek('Pak Lilik')
pak.pak_kepsek()

