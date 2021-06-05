#KELOMPOK 19
import json

print("=====================================")
print("         PROGRAM FRESH MART          ")
print("-------------------------------------")
print("Meneyediakan berbagai kebutuhan anda!")
print("       WE DELIVER YOUR NEEDS!         ")

total = []
Sayur = []
Buah = []
Ikan = []
Ayam = []
Sembako = []


def read_data():
    global data
    f = open('List Barang.json')
    data = json.load(f)

    f.close()


def pembeli():
    global nama
    global alamat
    global no_hp
    print("\n-------------------------------------")
    print("Selamat berbelanja di Fresh Mart.")
    print("Mohon isi data di bawah ini.")
    nama = input("Nama     : ")
    alamat = input("Alamat   : ")
    no_hp = input("No hp    : ")
    if len(no_hp) != 10 and len(no_hp) !=11:
        print("Maaf nomor handphone yang Anda masukkan tidak terdaftar.")
        print("Silahkan masukkan data Anda dengan benar untuk melanjutkan transaksi.")
        pembeli()
    else:
        read_data()
        print("\n--------------------------------------------------")
        daftar_barang()


def daftar_barang():
    global Sayur
    global Buah
    global Ikan
    global Ayam
    global Sembako
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
            global JumlahWortel
            Sayur = "Wortel"
            JumlahWortel = int(input("Masukkan jumlah wortel (kg) : "))
            TotalWortel = 20000 * JumlahWortel
            total.append(TotalWortel)
            tanya()
        elif KodeSayur == 2:
            global JumlahKentang
            Sayur = "Kentang"
            JumlahKentang = int(input("Masukkan jumlah kentang (kg) : "))
            TotalKentang = 18000 * JumlahKentang
            total.append(TotalKentang)
            tanya()
        elif KodeSayur == 3:
            global JumlahBawangBombay
            Sayur = "Bawang bombay"
            JumlahBawangbomay = int(input("Masukkan jumlah bawang bombay (kg) : "))
            TotalBawangbombay = 28000 * JumlahBawangbomay
            total.append(TotalBawangbombay)
            tanya()
        else:
            print("Maaf sayur belum tersedia.")
    elif kode == 2:
        print()
        print("Silahkan pilih buah yang Anda inginkan!")
        print(" Kode | Nama Buah   | Harga ")
        print("--------------------------------------------------")
        print(" 1    | Apel        | 40000")
        print(" 2    | Jeruk       | 15000")
        print(" 3    | Mangga      | 30000")
        KodeBuah = int(input("Masukkan kode buah: "))
        if KodeBuah == 1:
            Buah = "Apel"
            JumlahApel = int(input("Masukkan jumlah apel (kg) : "))
            TotalApel = 40000 * JumlahApel
            total.append(TotalApel)
            tanya()
        elif KodeBuah == 2:
            Buah = "Jeruk"
            JumlahJeruk = int(input("Masukkan jumlah jeruk (kg) : "))
            TotalJeruk = 15000 * JumlahJeruk
            total.append(TotalJeruk)
            tanya()
        elif KodeBuah == 3:
            Buah = "Mangga"
            JumlahMangga = int(input("Masukkan jumlah mangga (kg) : "))
            TotalMangga = 30000 * JumlahMangga
            total.append(TotalMangga)
            tanya()
        else:
            print("Maaf barang buah tersedia.")
    elif kode == 3:
        print()
        print("Silahkan pilih ikan yang Anda inginkan!")
        print(" Kode | Nama Ikan   | Harga ")
        print("--------------------------------------------------")
        print(" 1    | Ikan Gurame | 60000")
        print(" 2    | Ikan Nila   | 27000")
        print(" 3    | Ikan Kakap  | 90000")
        KodeIkan = int(input("Masukkan kode ikan: "))
        if KodeIkan == 1:
            Ikan = "Gurame"
            JumlahIkanGurame = int(input("Masukkan jumlah Ikan Gurame (kg) : "))
            TotalIkanGurame = 60000 * JumlahIkanGurame
            total.append(TotalIkanGurame)
            tanya()
        elif KodeIkan == 2:
            Ikan = "Nila"
            JumlahIkanNila = int(input("Masukkan jumlah Ikan Nila (kg) : "))
            TotalIkanNila = 27000 * JumlahIkanNila
            total.append(TotalIkanNila)
            tanya()
        elif KodeIkan == 3:
            Ikan = "Kakap"
            JumlahIkanKakap = int(input("Masukkan jumlah Ikan Kakap (kg) : "))
            TotalIkanKakap = 90000 * JumlahIkanKakap
            total.append(TotalIkanKakap)
            tanya()
        else:
            print("Maaf ikan belum tersedia.")
    elif kode == 4:
        print()
        print("Silahkan pilih ayam yang Anda inginkan!")
        print(" Kode | Nama Ayam     | Harga ")
        print("--------------------------------------------------")
        print(" 1    | Ayam Pejantan | 40000")
        print(" 2    | Ayam Boiler   | 35000")
        print(" 3    | Ayam Kampung  | 45000")
        KodeAyam = int(input("Masukkan kode ayam: "))
        if KodeAyam == 1:
            Ayam = "Ayam Pejantan"
            JumlahAyamPejantan = int(input("Masukkan jumlah Ayam Pejantan (kg) : "))
            TotalAyamPejantan = 40000 * JumlahAyamPejantan
            total.append(TotalAyamPejantan)
            tanya()
        elif KodeAyam == 2:
            Ayam = "Ayam Boiler"
            JumlahAyamBoiler = int(input("Masukkan jumlah Ayam Boiler (kg) : "))
            TotalAyamBoiler = 35000 * JumlahAyamBoiler
            total.append(TotalAyamBoiler)
            tanya()
        elif KodeAyam == 3:
            Ayam = "Ayam Kampung"
            JumlahAyamKampung = int(input("Masukkan jumlah Ayam Kampung (kg) : "))
            TotalAyamKampung = 45000 * JumlahAyamKampung
            total.append(TotalAyamKampung)
            tanya()
        else:
            print("Maaf ayam belum tersedia.")
    elif kode == 5:
        print()
        print("Silahkan pilih sembako yang Anda inginkan!")
        print(" Kode | Nama Sembako  | Harga ")
        print("--------------------------------------------------")
        print(" 1    | Beras         | 10500")
        print(" 2    | Telur         | 28000")
        KodeSembako = int(input("Masukkan kode sembako: "))
        if KodeSembako == 1:
            Sembako = "Beras"
            JumlahBeras = int(input("Masukkan jumlah Beras (kg) : "))
            TotalBeras = 10500 * JumlahBeras
            total.append(TotalBeras)
            tanya()
        elif KodeSembako == 2:
            Sembako = "Telur"
            JumlahTelur = int(input("Masukkan jumlah Telur (kg) : "))
            TotalTelur = 28000 * JumlahTelur
            total.append(TotalTelur)
            tanya()
            return
        else:
            print("Maaf sembako belum tersedia.")
    else:
        print("Maaf barang belum tersedia. Silahkan pilih barang yang tersedia.\n")
        daftar_barang()       
       
        
def tanya():
    print("\n--------------------------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("--------------------------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        pesanan()
    else:
        print("Pilihan yang anda masukan salah!")
        tanya()

        
def pesanan():
    print("Berikut adalah daftar pesanan Anda:")
    print("Sayur    : ", Sayur)
    print("Buah     : ", Buah)
    print("Ikan     : ", Ikan)
    print("Ayam     : ", Ayam)
    print("Sembako  : ", Sembako)
    Cek = input("Apakah pesanan Anda sudah benar? [y/t] : ")
    if Cek == "y":
        harga()
    elif Cek == "t":
        daftar_barang()
    else :
        print("Pilihan yang anda masukan salah!")
        pesanan()        

        
def harga():
    print("\n")
    harga = sum(total)
    print("Total pembelian : Rp ", harga)
    metode_pengiriman()


def metode_pengiriman():
    print("\n--------------------------------------------------")
    print("Silahkan memilih metode pengiriman yang tersedia.")
    print(" Kode | Metode Pengiriman ")
    print("--------------------------------------------------")
    print(" 1    | Paxel             ")
    print(" 2    | Gosend            ")
    KodePengiriman = int(input("Masukkan kode metode pengiriman : "))
    if KodePengiriman == 1:
        print("Anda akan dihubungi oleh kurir Paxel")
        metode_pembayaran()
    elif KodePengiriman == 2:
        print("Anda akan dihubungi oleh kurir Gosend")
        metode_pembayaran()
    else:
        print("Maaf metode pengiriman belum tersedia.")
        print("Anda harus memilih metode pengiriman yang tersedia.")
        metode_pengiriman()


def metode_pembayaran():
    print("\n--------------------------------------------------")
    print("Silahkan memilih metode pembayaran yang tersedia.")
    print(" Kode | Metode Pembayaran  ")
    print("--------------------------------------------------")
    print(" 1    | BCA                ")
    print(" 2    | GoPay              ")
    KodePembayaran = int(input("Masukkan kode metode pembayaran : "))
    if KodePembayaran == 1:
        print("Silahkan transfer ke 0329009779")
        akhir()
    elif KodePembayaran == 2:
        print("Silahkan transfer ke 0825333123")
        akhir()
    else:
        print("Maaf metode pembayaran belum tersedia.")
        print("Anda harus memilih metode pengiriman yang tersedia.")
        metode_pembayaran()


def akhir():
    print("\n\n-------------------------------------")
    print("=====================================")
    print("         PROGRAM FRESH MART          ")
    print("=====================================")
    print("     Detail Informasi Pembelian      ")
    print()
    print("Nama                 : ", nama)
    print("Alamat Pengiriman    : ", alamat)
    print("No hp                : ", no_hp)
    
    print()

pembeli()




