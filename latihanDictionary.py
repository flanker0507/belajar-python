import os
import random
import string

from datetime import datetime


mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '0000000000',
    'sks_lulus' : 0,
    'lahir' : datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print(f"-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input(f"Nama Mahasiswa: ")
    mahasiswa['nim'] = input(f"NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input(f"SKS Lulus = "))
    TAHUN_LAHIR = int(input(f"Tahun Lahir (YYYY)= "))
    BULAN_LAHIR = int(input(f"Bulan Lahir(1-12)= "))
    TANGGAL_LAHIR = int(input(f"Tanggal Lahir (1-31)= "))
    mahasiswa['lahir'] = datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'NAMA':<17} {'NIM':<9} {'SKS Lulus':<10} {'LAHIR':<10}")
    print(f"-" * 60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10}  {LAHIR:^10}")


    print("\n")
    operator = input(f"Mau Tambah Lagi Brooo ???(y/n)")
    if operator.lower() == "n":
        break

print(f"THANK YOU :)")
