def garis():
    print("-------------------------")


print("----- JDORS (Layanan hotel berjedor jedor)--")
print("------Silahkan untuk pilih tipe kamar-------")
print("-1--Regular--Rp.150.000/Malam----")
print("-2--VIP----Rp.300.000/malam----")
print("-3--VVIP----Rp.600.000/malam----")
print("-4--Kingdom--Rp.1.200.000/malam----")
print("---PROMO! NGINEP SEMINGGU BONUS SEHARI---")

#input dari customer
garis()
tipe = int(input("silahkan pilih tipe : "))
inap = int(input("Berapa Malam Mengingap : "))
cust = input("Masukan Nama Anda : ")

garis()       
if tipe == 1:
    tipe_kamar = ("Reguler")
elif tipe == 2:
    tipe_kamar = ("VIP")
elif tipe == 3:
    tipe_kamar = ("VVIP")
elif tipe == 4:
    tipe_kamar = ("Kingdom")
else :
    tipe_kamar = ("Yang bener??")

if tipe == 1:
    total_harga = inap * 150000  
elif tipe == 2:
    total_harga = inap * 300000
elif tipe == 3:
    total_harga = inap * 600000
elif tipe == 4:
    total_harga = inap * 1200000

print("Terima kasih" , cust ,"Atas menggunakan layanan kami")
print("Tipe kamar yang anda pilih" , tipe_kamar)
print("Total harga :Rp", total_harga)

if inap >= 7:
    print("SELAMAT ANDA MENDAATKAN BINUS 1 HARI")
    print("Terima Kasih telah menginap di JDOORS")
    total_inap = inap+1
elif inap < 7 :
    print("Terima Kasih telah menginap di JDOORS")
    total_inap = inap
print("Total lama menginap :Rp", total_inap, "Hari")     