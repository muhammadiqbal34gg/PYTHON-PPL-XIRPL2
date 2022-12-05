print("===============")
print("Daftar HP terbaru")
print("===============")
print("1.HP ROG Phone 7")
print("2.HP Iphone 15")
print("3.HP Samsung S23 Ultra")
print("===============")

bang = int(input("silahkan pilih hp : "))
warna = int(input("Mau warna ape : "))

if bang == 1:
    jenis = ("Reguler")
elif bang == 2:
    jenis = ("VIP")
elif bang == 3:
    jenis = ("VVIP")
else :
    jenis = ("Yang bener??")