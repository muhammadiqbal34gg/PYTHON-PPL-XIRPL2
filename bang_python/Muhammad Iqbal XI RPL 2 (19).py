class orang:
    def __init__(self, nama, Agama):
        self.nama = nama
        self.Agama = Agama

    def perkenalan(self):
        print(self.nama,"Beragama",self.Agama)

class Islam(orang):
    def __init__(self,nama, Agama, solat):
        orang.__init__(self, nama, Agama)
        self.solat = solat

class budha(orang):
    def __init__(self,nama , Agama, jangkrik):
        orang.__init__(self, nama, Agama)
        self.jangkrik = jangkrik

Dava = Islam('Dava','Islam','Sholat')
Dava.perkenalan()
print("Dava beribadah dengan melakukan", Dava.solat)

bongcin = budha('bongcin','budha','sembahyang')
bongcin.perkenalan()
print("bong cin beribadah dengan melakukan", bongcin.jangkrik)