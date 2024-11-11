import os


def header():
    '''Function Header'''
    os.system("clear")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''Function Input User'''
    # Mengambil input user
    lebar = int(input(f"Masukka nilai lebar = "))
    panjang = int(input(f"Masukka nilai panjang = "))

    return lebar, panjang

def hitung_luas(lebar, panjang):
    '''Function Luas'''
    return panjang * lebar

def hitung_keliling(lebar, panjang):
    '''FUnction Keliling'''
    return 2*(lebar+panjang)

def choice():
    '''Function to get user's choice'''
    print(f"\nPilih Operasi yang kau mau:")
    print(f"1. Mencari Luas")
    print(f"2. Mencari Keliling")
    print(f"3. Mencari Kedaunya")
    isInput = int(input("Masukkan Pilihan Anda (1,2 atau 3): "))
    return isInput

def display(message,value):
    '''Function Display'''
    print(f"Hasil Perhitungan {message} = {value}")

# Program Utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    user_choice = choice()

    if user_choice == 1:
        LUAS = hitung_luas(LEBAR, PANJANG)
        display("luas",LUAS)

    elif user_choice == 2:
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling", KELILING)

    elif user_choice == 3:
        LUAS = hitung_luas(LEBAR, PANJANG)
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("luas",LUAS)
        display("keliling", KELILING)

    else:
        print(f"PILIHAN TIDAK ADA")


    isCintinue = input("apakah mau lagi ? (y/n)")
    if isCintinue.lower()== "n":
        break
print("PROGRAM SELESAI")