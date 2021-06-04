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
    index = 1
    lst_barang = list(data.keys())
    print("Berikut barang yang tersedia di toko Fresh Mart")
    print(" Kode | Nama Barang ")
    print("--------------------------------------------------")
    for i in range(len(lst_barang)-2):
        print(f" {i+1:<4} | {lst_barang[i]:<15}")
    print("--------------------------------------------------")
    kode = int(input("Masukkan kode barang  : "))
    if kode == 1:
        print()
        print("Silahkan pilih sayur yang Anda inginkan!")
        print(" Kode | Nama Sayur      | Harga")
        print("--------------------------------------------------")
        for i in data["Sayur"]:
            nama = i["Nama"]
            harga = i["Harga"]
            print(f" {index:<4} | {nama:<15} | {harga:<15}")
            index += 1
        KodeSayur = int(input("Masukkan kode sayur: "))
        if KodeSayur == 1:
            JumlahWortel = int(input("Masukkan jumlah wortel (kg) : "))
            TotalWortel = 20000 * JumlahWortel
            Sayur.append(f"- Wortel sebanyak {JumlahWortel} kg seharga Rp{TotalWortel}")
            total.append(TotalWortel)
            tanya()
        elif KodeSayur == 2:
            JumlahKentang = int(input("Masukkan jumlah kentang (kg) : "))
            TotalKentang = 18000 * JumlahKentang
            Sayur.append(f"- Kentang sebanyak {JumlahKentang} kg seharga Rp{TotalKentang}")
            total.append(TotalKentang)
            tanya()
        elif KodeSayur == 3:
            JumlahBawangbombay = int(input("Masukkan jumlah bawang bombay (kg) : "))
            TotalBawangbombay = 28000 * JumlahBawangbombay
            Sayur.append(f"- Bawang bombay sebanyak {JumlahBawangbombay} kg seharga Rp{TotalBawangbombay}")
            total.append(TotalBawangbombay)
            tanya()
        else:
            print("Maaf sayur belum tersedia.")
            daftar_barang()
    elif kode == 2:
        print()
        print("Silahkan pilih buah yang Anda inginkan!")
        print(" Kode | Nama Buah       | Harga")
        print("--------------------------------------------------")
        for i in data["Buah"]:
            nama = i["Nama"]
            harga = i["Harga"]
            print(f" {index:<4} | {nama:<15} | {harga:<15}")
            index += 1
        KodeBuah = int(input("Masukkan kode buah: "))
        if KodeBuah == 1:
            JumlahApel = int(input("Masukkan jumlah apel (kg) : "))
            TotalApel = 40000 * JumlahApel
            Buah.append(f"- Apel sebanyak {JumlahApel} kg seharga Rp{TotalApel}")
            total.append(TotalApel)
            tanya()
        elif KodeBuah == 2:
            JumlahJeruk = int(input("Masukkan jumlah jeruk (kg) : "))
            TotalJeruk = 15000 * JumlahJeruk
            Buah.append(f"- Jeruk sebanyak {JumlahJeruk} kg seharga Rp{TotalJeruk}")
            total.append(TotalJeruk)
            tanya()
        elif KodeBuah == 3:
            JumlahMangga = int(input("Masukkan jumlah mangga (kg) : "))
            TotalMangga = 30000 * JumlahMangga
            Buah.append(f"- Mangga sebanyak {JumlahMangga} kg seharga Rp{TotalMangga}")
            total.append(TotalMangga)
            tanya()
        else:
            print("Maaf barang buah tersedia.")
            daftar_barang()
    elif kode == 3:
        print()
        print("Silahkan pilih ikan yang Anda inginkan!")
        print(" Kode | Nama Ikan       | Harga")
        print("--------------------------------------------------")
        for i in data["Ikan"]:
            nama = i["Nama"]
            harga = i["Harga"]
            print(f" {index:<4} | {nama:<15} | {harga:<15}")
            index += 1
        KodeIkan = int(input("Masukkan kode ikan: "))
        if KodeIkan == 1:
            JumlahIkanGurame = int(input("Masukkan jumlah Ikan Gurame (kg) : "))
            TotalIkanGurame = 60000 * JumlahIkanGurame
            Ikan.append(f"- Ikan Gurame sebanyak {JumlahIkanGurame} kg seharga Rp{TotalIkanGurame}")
            total.append(TotalIkanGurame)
            tanya()
        elif KodeIkan == 2:
            JumlahIkanNila = int(input("Masukkan jumlah Ikan Nila (kg) : "))
            TotalIkanNila = 27000 * JumlahIkanNila
            Ikan.append(f"- Ikan Nila sebanyak {JumlahIkanNila} kg seharga Rp{TotalIkanNila}")
            total.append(TotalIkanNila)
            tanya()
        elif KodeIkan == 3:
            JumlahIkanKakap = int(input("Masukkan jumlah Ikan Kakap (kg) : "))
            TotalIkanKakap = 90000 * JumlahIkanKakap
            Ikan.append(f"- Ikan Kakap sebanyak {JumlahIkanKakap} kg seharga Rp{TotalIkanKakap}")
            total.append(TotalIkanKakap)
            tanya()
        else:
            print("Maaf ikan belum tersedia.")
            daftar_barang()
    elif kode == 4:
        print()
        print("Silahkan pilih ayam yang Anda inginkan!")
        print(" Kode | Nama Ayam       | Harga")
        print("--------------------------------------------------")
        for i in data["Ayam"]:
            nama = i["Nama"]
            harga = i["Harga"]
            print(f" {index:<4} | {nama:<15} | {harga:<15}")
            index += 1
        KodeAyam = int(input("Masukkan kode ayam: "))
        if KodeAyam == 1:
            JumlahAyamPejantan = int(input("Masukkan jumlah Ayam Pejantan (kg) : "))
            TotalAyamPejantan = 40000 * JumlahAyamPejantan
            Ayam.append(f"- Ayam Pejantan sebanyak {JumlahAyamPejantan} kg seharga Rp{TotalAyamPejantan}")
            total.append(TotalAyamPejantan)
            tanya()
        elif KodeAyam == 2:
            JumlahAyamBoiler = int(input("Masukkan jumlah Ayam Boiler (kg) : "))
            TotalAyamBoiler = 35000 * JumlahAyamBoiler
            Ayam.append(f"- Ayam Boiler sebanyak {JumlahAyamBoiler} kg seharga Rp{TotalAyamBoiler}")
            total.append(TotalAyamBoiler)
            tanya()
        elif KodeAyam == 3:
            Ayam = "Ayam Kampung"
            JumlahAyamKampung = int(input("Masukkan jumlah Ayam Kampung (kg) : "))
            TotalAyamKampung = 45000 * JumlahAyamKampung
            Ayam.append(f"- Ayam Kampung sebanyak {JumlahAyamKampung} kg seharga Rp{TotalAyamKampung}")
            total.append(TotalAyamKampung)
            tanya()
        else:
            print("Maaf ayam belum tersedia.")
            daftar_barang()
    elif kode == 5:
        print()
        print("Silahkan pilih sembako yang Anda inginkan!")
        print(" Kode | Nama Sembako     | Harga")
        print("--------------------------------------------------")
        for i in data["Sembako"]:
            nama = i["Nama"]
            harga = i["Harga"]
            print(f" {index:<4} | {nama:<15} | {harga:<15}")
            index += 1
        KodeSembako = int(input("Masukkan kode sembako: "))
        if KodeSembako == 1:
            JumlahBeras = int(input("Masukkan jumlah Beras (kg) : "))
            TotalBeras = 10500 * JumlahBeras
            Sembako.append(f"- Beras sebanyak {JumlahBeras} kg seharga Rp{TotalBeras}")
            total.append(TotalBeras)
            tanya()
        elif KodeSembako == 2:
            JumlahTelur = int(input("Masukkan jumlah Telur (kg) : "))
            TotalTelur = 28000 * JumlahTelur
            Sembako.append(f"- Telur sebanyak {JumlahTelur} kg seharga Rp{TotalTelur}")
            total.append(TotalTelur)
            tanya()
            return
        else:
            print("Maaf sembako belum tersedia.")
            daftar_barang()
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
        cek_pesanan()
    else:
        print("Pilihan yang anda masukan salah!")
        tanya()


def pesanan():
    print("Berikut adalah daftar pesanan Anda:")
    if Sayur:
        print("Sayur    :")
        for i in Sayur:
            print(i)
    if Buah:
        print("Buah     : ")
        for i in Buah:
            print(i)
    if Ikan:
        print("Ikan     : ")
        for i in Ikan:
            print(i)
    if Ayam:
        print("Ayam     : ")
        for i in Ayam:
            print(i)
    if Sembako:
        print("Sembako  : ")
        for i in Sembako:
            print(i)

def cek_pesanan():
    Cek = input("Apakah pesanan Anda sudah benar? [y/t] : ")
    if Cek == "y":
        harga()
    elif Cek == "t":
        daftar_barang()
    else:
        print("Pilihan yang anda masukan salah!")
        pesanan()        

def harga():
    global harga
    print("\n")
    harga = sum(total)
    print("Total pembelian : Rp ", harga)
    metode_pengiriman()


def metode_pengiriman():
    global MetodePengiriman
    index = 1
    print("\n--------------------------------------------------")
    print("Silahkan memilih metode pengiriman yang tersedia.")
    print(" Kode | Metode Pengiriman ")
    print("--------------------------------------------------")
    for i in data["Metode Pengiriman"]:
        print(f" {index:<4} | {i:<15}")
        index += 1
    KodePengiriman = int(input("Masukkan kode metode pengiriman : "))
    if KodePengiriman == 1:
        MetodePengiriman = "Paxel"
        print("Anda akan dihubungi oleh kurir Paxel")
        metode_pembayaran()

    elif KodePengiriman == 2:
        MetodePengiriman = "Gosend"
        print("Anda akan dihubungi oleh kurir Gosend")
        metode_pembayaran()
    else:
        print("Maaf metode pengiriman belum tersedia.")
        print("Anda harus memilih metode pengiriman yang tersedia.")
        metode_pengiriman()


def metode_pembayaran():
    global MetodePembayaran
    index = 1
    print("\n--------------------------------------------------")
    print("Silahkan memilih metode pembayaran yang tersedia.")
    print(" Kode | Metode Pembayaran  ")
    print("--------------------------------------------------")
    for i in data["Metode Pembayaran"]:
        print(f" {index:<4} | {i:<15}")
        index += 1
    KodePembayaran = int(input("Masukkan kode metode pembayaran : "))
    if KodePembayaran == 1:
        MetodePembayaran = "BCA"
        print("Silahkan transfer ke 0329009779")
        akhir()
    elif KodePembayaran == 2:
        MetodePembayaran = "GoPay"
        print("Silahkan transfer ke 0825333123")
        akhir()
    else:
        print("Maaf metode pembayaran belum tersedia.")
        print("Anda harus memilih metode pembayaran yang tersedia.")
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
    print("--------------------------------------")
    pesanan()
    print("--------------------------------------")
    print("Total                :  Rp", harga)
    print("Metode Pengiriman    : ", MetodePengiriman)
    print("Metode Pembayaran    : ", MetodePembayaran)
    print("\nTerima kasih sudah berbelanja di Fresh Mart.")


pembeli()
