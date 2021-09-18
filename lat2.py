pil = 0

while pil < 4:
    print ("Selamat Datang Di Rumah Sakit Gigi")
    print ("----------------------------------")
    print("""Silahkan Pilih Menu
    1. untuk member
    2. untuk bukan member
    3. untuk keluar""")
    pil = int(input("Masukkan Pilihan anda : "))

    if pil == 1:
        tambal = int(input("Berapa Gigi Yang Ditambal ? : "))
        if tambal == 1:
            awal = 90000
            print("Total Harga Yang Harus Dibayar Adalah Rp. ",awal)
        elif tambal > 1:
            awal = 90000
            dst = 80000
            hasil = awal + (tambal * dst)
            print("Total Yang Harus Dibayar Adalah Rp. ",hasil)
    if pil == 2:
        tambal = int(input("Berapa Gigi Yang Ditambal? : "))
        if tambal == 1:
            awal = 100000
            print("Total Yang Harus Dibayar Adalah Rp. ",awal)
        elif tambal > 1:
            awal = 100000
            hasil = tambal * awal
            print("Total Yang Harus Dibayar Adalah Rp. ",hasil)
    elif pil == 3:
        break
else:
    print("Pilihan Tidak Ada Di Menu")