#KELOMPOK 19
print("=====================================")
print("         PROGRAM FRESH MART          ")
print("-------------------------------------")
print("Meneyediakan berbagai kebutuhan anda!")
print("       WE DELIVER YOUR NEEDS!         ")

total = []

print("\n-------------------------------------")
print("Selamat berbelanja di Fresh Mart.")
print("Mohon isi data di bawah ini.")
nama = input("Nama     : ")
no_hp = input("No hp    : ")
alamat = input("Alamat   : ")
print("\n--------------------------------------------------")


def daftar_barang():
    print("Berikut barang yang tersedia di toko Fresh Mart")
    print(" Kode | Nama Barang ")
    print("--------------------------------------------------")
    print(" 1    | Sayur       ")
    print(" 2    | Buah        ")
    print(" 3    | Ikan        ")
    print(" 4    | Ayam        ")
    print(" 5    | Sembako     ")
    print("--------------------------------------------------")
    kode = int(input("Masukkan kode barang  : "))
    if kode == 1:
        print()
        print("Silahkan pilih sayur yang Anda inginkan!")
        print(" Kode | Nama Sayur    | Harga ")
        print("--------------------------------------------------")
        print(" 1    | Wortel        | 20000 ")
        print(" 2    | Kentang       | 18000 ")
        print(" 3    | Bawang bombay | 28000 ")
        KodeSayur = int(input("Masukkan kode sayur: "))
        if KodeSayur == 1:
            JumlahWortel = int(input("Masukkan jumlah wortel (kg) : "))
            TotalWortel = 20000 * JumlahWortel
            total.append(TotalWortel)
            tanya()
        elif KodeSayur == 2:
            JumlahKentang = int(input("Masukkan jumlah kentang (kg) : "))
            TotalKentang = 18000 * JumlahKentang
            total.append(TotalKentang)
