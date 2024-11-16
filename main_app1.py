## TUTORIAL MEMBACA FILE EKSTERNAL

print(3*"=", " Membaca File TxT ", 3*"=")
file = open("data.txt",mode="r")

print(f"status read = {file.readable()}")
print(f"status write = {file.writable()}")

# baca seluruh file
print(file.read())

## baca per baris
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

## baca semua baris sebagai list
#print(file.readlines())

print(f"apakah file sudah di Close : {file.closed}")
file.close()
print(f"apakah file sudah di Close : {file.closed}")

## Salah satu teknik membuka file file di Python

print(3*"=", " Membaca File TxT dengan 'with' ", 3*"=")

with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah di Close : {file.closed}")

print(f"apakah file sudah di Close : {file.closed}")
