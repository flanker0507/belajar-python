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