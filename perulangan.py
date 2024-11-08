# # Perulangan (loop)
# from unicodedata import numeric
#
# # for kondisi:
# # aksi
#
# # ini dengan list
# angka2_list = [0,2,4,8,10] # ini adalah list
# for i in angka2_list:
#     print(f"angka ke - {i}")
#
# print("Akhi dari program 1 \n")
#
# # ini dengan range
# angka2_range = range(5)
# for i in angka2_range:
#     print(f"angka ke : {i+1}")
#
# print("Akhi dari program 2 \n")
#
# angka3_range = range(1,5)
# for i in angka3_range:
#     print(f"angka ke : {i}")
#
# print("Akhi dari program 3 \n")
#
# # menggunaka string
#
# data_str = ("saya ganteng habis")
#
# for i in data_str:
#     print(f"huruf ke : {i}")
#
# print("Akhi dari program 4 \n")
#
# # While Loop
#
# # while loop :
# # aksi ini
# # aksi itu
#
# # akhir dari program
#
# angka = 0
# print(f"angka sekarang -> {angka}")
#
# while angka < 5:
#     angka += 1
#     print(f"angka sekarang -> {angka}")
#     print("otong kece maximallll")
#
# print("CUKYUPPPP")
#
# a = 0
# while a < 5 :
#     a += 1
#     print(a)

# continue, pass, break

# pass -> dia berfungsi sebagai dumy, tidak akan di eksekusi

# angka = 0
#
# while angka < 10:
#     angka += 1
#
#     if angka == 3:
#         print("yuda")
#         pass # tidak akan di eksekusi
#
#     print(angka)

# continue

# angka = 0
#
# print(f"angka sekarang -> {angka}")
#
# while angka < 5:
#     angka += 1
#     print(f"angka sekarang -> {angka}") #
#
#     if angka == 3:
#         print("NICE !")
#         continue # aksi langsung loncat ke step berikutnya
#
#     print("taiiii")
#
# print("pinish")

# Break

# angka = 0
#
# while angka < 5:
#     angka += 1
#     print(f"angka sekarang -> {angka}")
#
#     if angka == 3:
#         print("NICE !!!")
#         break
#
#     print("WADAPPPP")
#
#     print("cukuppp pinishh")
#

data_int = int(input("hitung sampai = "))

angka = 0

while True :
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        break