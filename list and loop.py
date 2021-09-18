import random as rd
# Memasukkan List User
data = {'Kevin':['Oergairu','Seishun Buta Yaro','Sangatsu no Lion'],
        'Daniel':['Re:Zero','Mushoku Tensei','Sword Art Online'],
        'Natalie':['Kimi no Nawa','Tenki no Ko','Violet Evergarden']}
pil = 0
# Proses Memasukkan Input Pemilik
user = (input("Masukkan Nama Pemilik : "))
# Jika Input Yang Dimasukkan Terdapat Di Data, maka dilakukan proses while
if user in data:
# While dilakukan jika pil masih kurang dari 7
    while pil<7:
        print("=================================")
    # Proses Pembuatan Menu
        print("""Selamat Datang Di Menu Crunchyroll
                1. Tampil Anime
                2. Menonton Anime
                3. Menambah Anime
                4. Hapus Anime
                5. Random Anime
                6. Keluar """)
        # pil akan diubah dari string ke int dengan menggunakan perintah int
        pil=int(input("Pilih Menu : "))
        if pil == 1:

        # data[user] dipakai untuk merujuk kepada user yang sudah dipilih diawal
        # perintah sep="\n" digunakan untuk membuat setiap list tersusun secara vertikal atau membuat baris baru

            print(data[user], sep="\n")
        elif pil == 2:
            print(data[user], sep="\n")

        # Angka pada Input juga diubah dari string menjadi int agar dapat disupport oleh len

            tonton = int(input("Pilih Anime Yang Akan Anda Tonton, gunakan angka 1/2/3/... "))
            if tonton <= len(data[user]):
                print ("Anime yang ditonton adalah",data[user][tonton-1])
            else:
                print("Anime Tidak Tersedia")
        elif pil == 3:
            data[user].insert(1,input("Masukkan Judul Anime : "))
            print("Anime Berhasil Ditambahkan")
        elif pil == 4:

            # del digunakan untuk menghapus data dari list

            print(data[user], sep="\n")
            hapus = int(input("Anime apa yang ingin anda hapus? gunakan angka 1/2/3/... "))
            del data[user][hapus-1]
            print("Anime Berhasil Dihapus")
        elif pil == 5:

            #rd.random digunakan untuk dapat membuat playlist diputar secara acak

            acak = int(rd.random()(len(data[user])))
            print("Anime Yang Sedang Diputar Adalah : ",data[user][acak])
        elif pil == 6:
            #Break digunakan untuk menyelesaikan program yang berjaln
            break
else:
    print("Nama Tidak Ditemukan")