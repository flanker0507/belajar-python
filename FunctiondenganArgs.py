'''*args'''
from datetime import datetime
from os import times


# memasukkan data/argument

def fungsi(name,height,weight):
    print(f"{name} punya tinggi {height} dan berat {weight}")

fungsi("ucup", 178,89)

def fungsi(data_list):
    data = data_list.copy()
    name = data[0]
    height = data[1]
    weight = data[2]

    print(f"{name} punya tinggi {height} dan berat {weight}")

fungsi(["Dilla", 150,55])

# studi kasus

def tambah(*data):
    # data tipe nya tuple, dia bisa di iterasi
    output = 0
    for i in data:
        output += i

    return output

result = tambah(1,2,3)
print(f"Hasilnya = {result}")

result = tambah(69,1)
print(f"Hasilnya = {result}")

'''kwargs'''

def fungsi(**kwargs):
    '''Fungsi Kwargs'''
    name = kwargs["name"]
    height = kwargs["height"]
    weight = kwargs["weight"]
    print(f"{name} punya tinggi {height} dan berat {weight}")

fungsi(name="Yuda", height=165, weight=65)

# studi kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("TIDAK ADA")

    return output

result = math(1,2,3,4,option="tambah")
print(f"hasil tambah {result}")

result = math(1,2,3,4,option="kali")
print(f"hasil kali {result}")
