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
            tanya()
        elif KodeSayur == 3:
            JumlahBawangbomay = int(input("Masukkan jumlah bawang bombay (kg) : "))
            TotalBawangbombay = 28000 * JumlahBawangbomay
            total.append(TotalBawangbombay)
            tanya()
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
            JumlahApel = int(input("Masukkan jumlah apel (kg) : "))
            TotalApel = 40000 * JumlahApel
            total.append(TotalApel)
            tanya()
        elif KodeBuah == 2:
            JumlahJeruk = int(input("Masukkan jumlah jeruk (kg) : "))
            TotalJeruk = 15000 * JumlahJeruk
            total.append(TotalJeruk)
            tanya()
        elif KodeBuah == 3:
            JumlahMangga = int(input("Masukkan jumlah mangga (kg) : "))
            TotalMangga = 30000 * JumlahMangga
            total.append(TotalMangga)
            tanya()
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
            JumlahIkanGurame = int(input("Masukkan jumlah Ikan Gurame (kg) : "))
            TotalIkanGurame = 60000 * JumlahIkanGurame
            total.append(TotalIkanGurame)
            tanya()
        elif KodeIkan == 2:
            JumlahIkanNila = int(input("Masukkan jumlah Ikan Nila (kg) : "))
            TotalIkanNila = 27000 * JumlahIkanNila
            total.append(TotalIkanNila)
            tanya()
        elif KodeIkan == 3:
            JumlahIkanKakap = int(input("Masukkan jumlah Ikan Kakap (kg) : "))
            TotalIkanKakap = 90000 * JumlahIkanKakap
            total.append(TotalIkanKakap)
            tanya()
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
            JumlahAyamPejantan = int(input("Masukkan jumlah Ayam Pejantan (kg) : "))
            TotalAyamPejantan = 40000 * JumlahAyamPejantan
            total.append(TotalAyamPejantan)
            tanya()
        elif KodeAyam == 2:
            JumlahAyamBoiler = int(input("Masukkan jumlah Ayam Boiler (kg) : "))
            TotalAyamBoiler = 35000 * JumlahAyamBoiler
            total.append(TotalAyamBoiler)
            tanya()
        elif KodeAyam == 3:
            JumlahAyamKampung = int(input("Masukkan jumlah Ayam Kampung (kg) : "))
            TotalAyamKampung = 45000 * JumlahAyamKampung
            total.append(TotalAyamKampung)
            tanya()
    elif kode == 5:
        print()
        print("Silahkan pilih sembako yang Anda inginkan!")
        print(" Kode | Nama Sembako  | Harga ")
        print("--------------------------------------------------")
        print(" 1    | Beras         | 10500")
        print(" 2    | Telur         | 28000")
        KodeSembako = int(input("Masukkan kode sembako: "))
        if KodeSembako == 1:
            JumlahBeras = int(input("Masukkan jumlah Beras (kg) : "))
            TotalBeras = 10500 * JumlahBeras
            total.append(TotalBeras)
            tanya()
        elif KodeSembako == 2:
            JumlahTelur = int(input("Masukkan jumlah Telur (kg) : "))
            TotalTelur = 28000 * JumlahTelur





