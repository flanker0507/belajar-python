import os

os.system("clear")
def hellow_world():
    print("Yuda Ganteng")
    print("Yuda Handsome")

hellow_world()

''' Fungsi dengan argument (input) '''

def hello_world(name):
    '''Fungsi hello world menerima input dengan variable name'''
    print(f"Selamat datang dunia wahai {name}")

hello_world("Asep")
hello_world("Ucup")

# program tambah

def tambah(angka_1, angka_2):
    '''Fungsi Tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,8)
tambah(90,87)

def say_hi(list_peserta):
    '''Fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ['Ucup', 'Asep', 'Dudung']

say_hi(anggota_boyband)

''' Fungsi dengan return '''

# template fungsi dengan return
# def name_func(argument):
#           body funch
#           return output

# function kuadrat

def kuadrat(input_angka):
    '''Function Kuadrat'''
    output_angka = input_angka**2
    return output_angka

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka_1, angka_2):
    '''fungsi return dengan fungsi input'''
    return angka_1 + angka_2

a = fungsi_tambah(1,8)
print(a)

def operasi_aritmatika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_aritmatika(8,10)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")

'''Default Argumen'''

# def function(argument):
# def function(argument = nilai default)

# contoh 1
def say_hello(name = "Ganteng"):
    '''Function default argument'''
    print(f"hai {name}")

say_hello("Ini Argument")
say_hello()

# contoh 2
def sapa_dia(name, message = "Apa Kabar ?"):
    '''Function dengan satu input biasa dan default argument'''
    print(f"Hai {name}, {message}")

sapa_dia("Dilla", "Aku KANGENNNNN")
sapa_dia("Ade")

# contoh 3
def hitung_pangkat(angka, pankat = 2):
    hasil = angka**pankat
    return hasil

print(hitung_pangkat(8,2))

hasil = hitung_pangkat(pankat=3, angka=5)
print(hasil)

# contoh 4

def fungsi(i1=1,i2=2,i3=3,i4=4):
    hasil = i1  + i2 + i3 + i4
    return hasil

print(fungsi())
print(fungsi(i2=4))
hasil = fungsi(i4=1)
print(hasil)

