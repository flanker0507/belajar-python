# Lambada Function
import os

os.system("clear")
def f_kuadrat(angka):
    return angka**2

print(f"Hasil Function Kuadrat = {f_kuadrat(5)}")

# Kita Coba Dengan Lamda
# output = lamda argument : expression

kuadrat = lambda angka : angka**2
print(f"Hasil Lamda Kuadrat = {kuadrat(6)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil Lamda Pangkta = {pangkat(4,3)}")

# kegunaan

# sorting list biasa
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting pakai len/panjang
def panjang_nama(name):
    return len(name)

data_list.sort(key=panjang_nama)
print(f"sorted list by len = {data_list}")

# sort pakai lamda
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda name:len(name))
print(f"sorted list by lamda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print(f"Menggunakan Lamda = {data_angka_baru}")

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(f"data genap = {data_genap}")

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0), data_angka))
print(f"data ganjil = {data_ganjil}")

# kelipatan 3
data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(f"kalipatan 3 = {data_3}")

# anonymous function
# currying <- Haskell Curry

def pangkat(angka,n):
    result = angka**n
    return result

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka : angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"pangkat2 = {pangkat3(5)}")
print(f"Pangkat Bebas = {pangkat(4)(5)}")