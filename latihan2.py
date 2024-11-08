print(f"*"*5 + "Program List Buku Dosa" + 5 * "*")

list_buku = []
while True :
    judul = input(f"Masukkan Judul Buku\t= ")
    penulis = input(f"Masukka Nama Penulis\t= ")

    data = [judul, penulis]
    list_buku.append(data)

    print(f"Judul = {data[0]}, Penulis = {data[1]}")

    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    operator = input(f"Apakah Akan Mencari Lagi ?(yes/no)")
    if operator != "yes":
        break