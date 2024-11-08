print(f"+"*3 + "Looping Dari List"+3*"+" +"\n")

print(f"+"*3 + "Menggunakan For Loop"+3*"+")
kumpul_angka = [1,2,3,4,5,6]
for i in kumpul_angka:
    print(f"angka ke - {i}")

peserta = ["Yuda", "Wira", "Pratama", "Handsome", "Sekali"]
for i in peserta:
    print(f"Nama Peserta = {i}")

print(f"+"*3 + "Menggunakan For Loop dengan Range"+3*"+")
kumpul_angka = [1,2,3,4,5,6]
panjang = len(kumpul_angka)

for i in kumpul_angka:
    print(f"angka ke - {i}")

print(f"+"*3 + "Menggunakan While Loop"+3*"+")

kumpul_angka = [1,2,3,4,5,6]
panjang = len(kumpul_angka)
i = 0
while i < panjang:
    print(f"angka ke - {kumpul_angka[i]}")
    i+=1

print(f"+"*3 + "List Comperhension"+3*"+")
peserta = ["Yuda", "Wira",69,96, "Pratama", "Handsome", "Sekali"]

[print(f"data = {i}") for i in peserta]

kumpul_angka = [1,2,3,4,5,6]

angka_kuadrar = [i**2 for i in kumpul_angka]
print(f"Angka Kuadrat {angka_kuadrar}")

print(f"+"*3 + "Enumerte"+3*"+")
peserta = ["Yuda", "Wira",69,96, "Pratama", "Handsome", "Sekali"]

for index, data in enumerate(peserta):
    print(f"index = {index}, data = {data}")




