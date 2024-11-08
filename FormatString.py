# contoh generic
# string
from statistics import fmean

name = "UCUP"
format_str = f"hello {name}"

print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)


# angka
angka = 2005.5
format_str = f"angka = {angka} "
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 20000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f} "
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f} "
print(format_str)

# menampilkan data + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan opersai aritmatika di dalam placeholder
harga = 10000
jumalah = 5

format_string = f"harga total = Rp. {harga*jumalah:,}"
print(format_string)

# format angka lain (binary, oactal, hexadecimal)

angka = 255
binary = f"binary = {bin(angka)}"
octal = f"octal = {oct(angka)}"
hex = f"hex = {hex(angka)}"

print(binary, "\n",octal,"\n", hex)

