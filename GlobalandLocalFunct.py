## Global and Local scope
import os

from ManipulasiString import name_lengkap

os.system("clear")

name_global = "Otong" # <- ini variable global

# akses varibel global dalam Function
def fungsi1():
    print(f"fungsi menampilkan {name_global}")

fungsi1()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {name_global}")

# percabangan
if True:
    print(f"if menampilkan {name_global}")

## Variable Local Scope

def fungsi2():
    name_local = "Ucup" # variable Local Scope
    return name_local

result = fungsi2()
print(result)
#print(name_local) # tidak bisa dilakukan bos

## Contoh 1: penggunaan akses variable
def say_otong():
    print(f"Hello {name}")

name = "Dilla"
say_otong()

## Contoh 2: Merubah variable global
angka = 0
name = "Yuda"

def ubah(nilai_baru, name_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = name_baru

print(f"Sebelum {angka,name}")
ubah(10,"Otong")
print(f"Setelah {angka,name}")

# contoh 3

angka = 0

for i in range(0,4):
    angka += i
    angka_dumy = 0

print(angka)
print(angka_dumy)

if True:
    angka = 5
    angka_dumy = 10

print(angka)
print(angka_dumy)