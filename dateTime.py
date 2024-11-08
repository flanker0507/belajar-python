# Data and Time (latihan)

import datetime as dt

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Masukkan Tanggal \t: "))
bulan = int(input("Masukkan Bulan \t\t: "))
tahun = int(input("Masukkan Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")