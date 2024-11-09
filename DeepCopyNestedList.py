from statistics import fmean

data_0 = [0,1]
data_1 = [2,3]

data_2D = [data_0, data_1,10]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")


print(f"+"*3+" Mengambil Data dari Nested List "+3*"+")
data = data_2D[0][1] # 0 data pertama dan 1 data ke dua lis
print(f"data = {data}")

print(f"+"*3+" Address Semuanya "+3*"+")
print(f"Address Asli = {hex(id(data_2D))}")
print(f"Address Copy = {hex(id(data_2D_copy))}")

print(f"+"*3+" Address Isi List "+3*"+")
print(f"Address Asli = {hex(id(data_2D[0]))}")
print(f"Address Copy = {hex(id(data_2D_copy[0]))}")

data_2D[0][1] = 9 # 0 data pertama dan 1 data ke dua list
data_2D[2] = 8
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

print(f"\n"+"+"*3+" DEEP COPY "+3*"+")

from copy import deepcopy

data_2D = [data_0, data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Address Asli = {hex(id(data_2D))}")
print(f"Address Deep Copy = {hex(id(data_2D_deepcopy))}")

print(f"+"*3+" Address Isi List "+3*"+")
print(f"Address Asli = {hex(id(data_2D[0]))}")
print(f"Address Deep Copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 90
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep copy = {data_2D_deepcopy}")







