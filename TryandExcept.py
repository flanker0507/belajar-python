# exception akan terjadi saat program mengalami error saat runtime

# contoh sederhana untuk menangkap exception
from math import nan


## contoh sederhana
# input_user = int(input("masukkan angka = "))
# hasil = nan
#
# try:
#     hasil = 10 /input_user
# except:
#     print("input tidak boleh 0")
#
# print(f"hasil = {hasil}")

while(True):
    angka = int(input("masukkan angka pembagi = "))
    try:
        hasil = 10 / angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan ?(y/n)")
        if is_done.lower() == "n":
            break
    except:
        print("pembagi nol, silahkan masukkan input lagi")
print("Akhir dari program 1")

# contoh aplikasi untuk membuat file data.txt

try:
    with open("data.txt","r") as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt","w",encoding='utf-8')as file:
        file.write("file baru")

print("Akhir dari program 2")