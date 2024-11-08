# # Latihan menbuat Segitiga
# from itertools import count
# #
# # # for
print("awal dari for")
sisi = 5

count = 1
for i in range(sisi):
    print("+"*count)
    count += 1

print("akhir dari for")
# # while
print("awal dari while")

count = 1

while True :
    print("+"*count)
    count += 1

    if count > sisi :
        break

print("akhir dari while")

 # while ganjil

print("awal dari while")
sisi = 10
count = 1
spasi = sisi

#  Bagian atas belah ketupat
while count <= sisi:
    if count % 2 != 0:  # Hanya untuk jumlah ganjil
        print(" " * spasi + "+" * count)
        spasi -= 1
    count += 1

# Bagian bawah belah ketupat
count = sisi - 2
spasi = 2

while count > 0:
    if count % 2 != 0:  # Hanya untuk jumlah ganjil
        print(" " * spasi + "+" * count)
        spasi += 1
    count -= 1

print("akhir dari while")

sisi =  9 # Ukuran harus ganjil untuk hasil yang simetris
count = 1
spasi = sisi // 2
print(spasi)

# Bagian atas belah ketupat
while count <= sisi:
    if count % 2 != 0:  # Hanya mencetak jumlah ganjil dari +
        print(" " * spasi + "+" * count)
        spasi -= 1  # Mengurangi spasi untuk baris berikutnya
    count += 1

# Bagian bawah belah ketupat
count = sisi -2
spasi = 1

while count > 0:
    if count % 2 != 0:  # Hanya mencetak jumlah ganjil dari +
        print(" " * spasi + "+" * count)
        spasi += 1  # Menambah spasi untuk baris berikutnya
    count -= 1

from codecs import Codec
from itertools import count

sisi = 9
count = 1
spasi = sisi // 2

while True:
    # print jika ganjil
    if (count % 2 != 0) :
        print(" " * spasi + "+" * count)
        spasi -= 1
        count += 1

    else:
        count += 1
        continue


    if count > sisi:
        break

count = sisi - 2
spasi = 1
while True:
    if (count %2 != 0):
        print(" " * spasi + "+" * count)
        spasi += 1
        count -= 1

    else:
        count -= 1
        continue

    if count < 0:
        break


