#PROGRAM SISTEM MANAJEMEN DAFTAR KARYAWAN MIE GACOAN

print("="*61)
print("DASAR DASAR PEMPROGRAMAN")
print("MINI PROJECT 1")
print("AULIA SHEVA SAVITRI | 2509116001")
print("="*61)  

#TAMPILAN UTAMA
print("DATA KARYAWAN DI MIE GACOAN")
print("="*61)
print("MENU UTAMA")
print("1. Tambah Karyawan Baru")
print("2. Lihat Semua Karyawan")
print("3. Ubah Data Karyawan")
print("4. Hapus Data Karyawan")
print("5. Keluar")
print("="*61)

#PROGRAM
pilihan = input("masukkan nomor (1-5): ")
Karyawan =  [
    ("ipul", "Kasir", "Pagi", "4500000"),
    ("Iput", "Koki", "Sore", "5500000"),
    ("Selamet kopling", "Pelayan", "Malam", "4000000"),
    ("Cece bento", "pelayan", "Pagi", "4000000"),
    ("Ucup Niagara Fruit", "Koki", "Malam", "6000000")
    ]
#PROGRAM TAMBAHAN KARYAWAN BARU
if pilihan == '1' :
    nama = input("Masukkan nama karyawan: ")
    posisi = input("Masukkan posisi: ")
    shift = input("Masukkan shift: ")
    gaji = input("Masukkan gaji: ")
    if not nama or not posisi or not shift or not gaji:
            print("Error: Semua field harus diisi!")
    else:
            data_karyawan = (nama, posisi, shift, gaji)
            Karyawan.append(data_karyawan)
            print(f"Data karyawan {nama} berhasil ditambahkan!")
#LIHAT SEMUA KARYAWAN
elif pilihan == '2':
    if not Karyawan :
        print("Tidak ada data karyawan.")
    else:
        print("Daftar Karyawan Mie Gacoan:")
        print("=" * 61)
        print(f"‖ {'No.':^2} | {'Nama':^18} | {'Posisi':^8} | {'Shift':^6} | {'Gaji':^11}‖")
        print("=" * 61)
        for i, k in enumerate(Karyawan, 1):
            print(f"‖ {i:<3} | {k[0]:<18} | {k[1]:<8} | {k[2]:<6} | Rp {k[3]:<8}‖")
        print("=" * 61)
#UBAH DATA KARYAWAN
elif pilihan == '3':
    if not Karyawan:
        print("Tidak ada data yang di ubah.")
    else:
        print("Daftar Karyawan Mie Gacoan:")
        print("=" * 61)
        print(f"‖ {'No.':^2} | {'Nama':^18} | {'Posisi':^8} | {'Shift':^6} | {'Gaji':^11}‖")
        print("=" * 61)
        for i, k in enumerate(Karyawan, 1):
            print(f"‖ {i:<3} | {k[0]:<18} | {k[1]:<8} | {k[2]:<6} | Rp {k[3]:<8}‖")
        print("=" * 61)
        
        index_input = input("Pilih nomor karyawan yang ingin diubah: ")
        if index_input.isdigit():
            index = int(index_input) - 1
            if index >= 0 and index < len(Karyawan):
                nama = input("Masukkan nama baru: ")
                posisi = input("Masukkan posisi baru: ")
                shift = input("Masukkan shift baru: ")
                gaji = input("Masukkan gaji baru: ")
                if not nama or not posisi or not shift or not gaji:
                    print("Error: Semua field harus diisi!")
                else:
                    Karyawan[index] = (nama, posisi, shift, gaji)
                    print(f"Data karyawan berhasil diubah!")
            else:
                print("Nomor tidak valid!")
        else:
            print("Input harus berupa angka!")
#HAPUS DATA KARYAWAN
elif pilihan == '4' :
    if not Karyawan:
        print("Tidak ada data karyawan")
    else:
        print("Daftar Karyawan Mie Gacoan:")
        print("=" * 61)
        print(f"‖ {'No.':^2} | {'Nama':^18} | {'Posisi':^8} | {'Shift':^6} | {'Gaji':^11}‖")
        print("=" * 61)
        for i, k in enumerate(Karyawan, 1):
            print(f"‖ {i:<3} | {k[0]:<18} | {k[1]:<8} | {k[2]:<6} | Rp {k[3]:<8}‖")
        print("=" * 61)
        index_input = input("Pilih nomor karyawan yang ingin di hapus:")
        if index_input.isdigit ():
            index = int(index_input) -1
            if index >= 0 and index < len(Karyawan):
                hapus = Karyawan.pop(index)
                print(f"Data karyawan {hapus[0]} berhasil dihapus!")
            else:
                print("Nomor tidak valid!")
        else:
            print("Input harus berupa angka!")
#KELUAR
elif pilihan == '5' :
    print("Terimakasih telah telah menggunakan sistem ini.")
else:
    print("Pilihan tidak valid! Silakan masukkan angka 1-5.")