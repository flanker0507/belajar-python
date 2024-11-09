## --- LIST ---

data = [0,1,2,3,4,5]
print(data)

data = range(1,5)
for i in data:
    print(i)

# cara alternatif membuat list
dat_range = range(0,10,2) # range(start, stop, step)
print(dat_range)
data_list = list(dat_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_menggunakan_for = [i for i in range(0,10)]
print(list_menggunakan_for)

# membuat list pakai for dan if
list_use_for_if = [i for i in range(0,10) if i != 5]
print(list_use_for_if)

list_use_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_use_for_if)

list_use_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_use_for_if)

# index     0(-3),  1(-2),  2(-1)
data1 = ["otong", "ucup", "dadang"]

# mengambil data dari list
data0 = data1[0]
print(f"data pertama index 0 = {data0}")

data_terakhir = data1[-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah index dalam list
panjang_data = len(data1)
print(f"panjang data 1 adalah = {panjang_data}")

## Manipulasi Data List

# menambah item pada list sesuai kondisi
print(f"data sebelum di tambah \n{data1}")

data1.insert(1, "Asep")
print(f"data sesudah di tambah \n{data1}")

# menambah di akhir list
data1.append("jajang")
print(f"data di tambah lagi \n{data1}")

# menambah list dengan list
data_baru = ["yuda", "wira", "pratama"]
data1.extend(data_baru)
print(f"data gabungan \n{data1}")

# merubah data
data1[2] = "Michael"
print(f"data rubah \n {data1}")

# meremove data
data1.remove("Asep")
print(f"data remove \n{data1}")

# meremove data paling belakang
data_belakang = data1.pop()
print(f"remove data belakang \n {data1}")
print(f"data belakang \n {data_belakang}")

data_angka = [1,2,3,4,5,3,2,3,5,6,8,9,7,0]

print(f"data angka \n {data_angka}")

# count data

jumlah_data_5 = data_angka.count(5)
print(f"jumlah angka 5 adalah {jumlah_data_5}")

# ambil posisi index data
database = ["Yuda", "Wira", "Pratama", "Ganteng"]
print(f"data = {database}")

index_pratama = database.index("Pratama")
print(f"Index sih Pratama adalah {index_pratama}")

# mengurutkan list
print(f"data angka sebelum sort \n {data_angka}")
data_angka.sort()
print(f"Data angka setelah sort \n {data_angka}")

# balik list (reverse)
data_angka.reverse()
print(f"Data Reverse : \n {data_angka}")

## Teknik menduplikat list

a = ["Yuda", "Wira", "Pratama"]
print(f"a = {a}")

b = a # Pas By Reference
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[0] = "Ganteng"
a.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copt
print(f"="*5 + " membuat list c dengan a.copy" + "="*5)
c = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"="*5 + " Kita Ubah Data Index Ke - 0 " + "="*5)
c[0] = "Yuda"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"\n"+"="*5 + " Nested List " + "="*5)

data0 = [1,2,0,4]
data1 = [9,8,7]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data0, data1, 6, 7]

print(f"list 2D = {list_2D}")

print(f"="*5 + " Cara Penggunaan Nested List " + "="*5)

peserta0 = ["ucup", 25, "laki-laki"]
peserta1 = ["otong", 10, "laki-laki"]
peserta2 = ["dedeh", 50, "wanita"]

list_peserta = [peserta0, peserta1, peserta2]

print(f"Peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Name\t: {peserta[0]}")
    print(f"Age\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")







