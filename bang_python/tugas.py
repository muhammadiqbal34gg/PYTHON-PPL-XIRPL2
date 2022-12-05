class kalkulator:
    def __init__(self, siji, loro):
        self.siji = siji
        self.loro = loro
    def __str__(self):
        hasil = self.siji + self.loro
        return f'Hasil dari {self.siji} + {self.loro} adalah : {hasil}'
    
a = angka(int(input("masukkan angka pertama:")), int(input("masukkan angka dua")))
print(a)