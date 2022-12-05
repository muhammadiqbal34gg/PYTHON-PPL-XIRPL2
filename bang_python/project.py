#input data
stock = {}
#dengan struktur {id : 'jenis_barang','merk_barang','qty'}
#Home
def garis():
	print('='*29)

def menu_awal():
	garis()
    print("   CRUD SYSTEM    ")
    garis()
    print("Selamat datang di aplikasi CRUD")
    print("Gudang kami bisa menyimpan barang anda")
    print("Sesuai kebutuhan anda")
    garis()
    
def menu():
	print("=Storage Management Menu=")
    garis()
    print("(1) - input Barang")
	print("(2) - Ambil barang")
    print("(3) - Cel barang")
    print("(4) - End program")
    return int(input("= "))

run = menu_awal()
run = menu()

#Data
class sistem:
    while True:
        if run == 1:
            auth1 = int(input("Barang baru : 1 atau barang lama : 2 ?"))
            if auth1 == 1: 
                id_barang = int(input("Masukkan id barang ="))
                jenis_barang = input("Masukkan jenis barang =") 
                merk_barang = input("Masukkan merk barang =") 
                qty_barang = int(input("Masukkan qty barang ="))
                garis()
                stock[id_barang] = jenis_barang, merk_barang, qty_barang
                print(stock[id_barang])
                print("Barang berhasil di tambah")
                choice = int(input("ketik 4 jika ingin n"))
                input("ketik 4 untuk lanjut atau ketik 5 untuk keluar")
                if choice == 4:
                    run = menu()
                else:
                    break
            elif run == 2:
                print("Fitur masih dalam pengembangan")
        elif run == 3:
            print("BARANG YANG TERSEDIA")
            print("-id barang--jenis--merk--qty--")
            for key,value in stock.items():
                print("{}:{}".format(key,value))
            garis()
            choice = int(input("ketik 4 jika ingin n"))
                input("ketik 4 untuk lanjut atau ketik 5 untuk keluar")
            if choice == 4:
                run = menu()
            else:break
            

#Tambah data
#Update data
#Delete data