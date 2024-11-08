# kalkulator sederhana
from aritmatika import hasil

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukkan angka 1: "))
angka_2 = float(input("Masukkan angka 2: "))

operator = input("Masukkan operator (+, -, x, /): ")


# percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("MASUKKAN YANG BENER DONKKK")

print("END")