# operasi dan manipulasi string

# 1. menyambung string (concatenate)
name_pertama = "ucup"
name_kedua = "D"
name_ketiga = "Fame"

name_lengkap = name_pertama + " "+ name_kedua + "'"+ name_ketiga
print(name_lengkap)

# 2. Menghitung panjang string
panjang = len(name_lengkap)
print("panjang dari "+ name_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in name_lengkap
print(d + " ada di " + name_lengkap + " = " + str(status))

D = "D"
status = D in name_lengkap
print(D + " ada di " + name_lengkap + " = " + str(status))

d = "d"
status = d not in name_lengkap
print(d + " tidak ada di " + name_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + name_lengkap[0])
print("index ke-6 : " + name_lengkap[6])
print("index ke-(-1) : " + name_lengkap[-1])
print("index ke-(-2) : " + name_lengkap[-2])
print("index ke-[0:3] : " + name_lengkap[0:3])
print("index ke-[3:7] : " + name_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] : " + name_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(name_lengkap))
# item paling besar
print("paling besar : " + max(name_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " +str(jumlah))

# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# mengubah ke lower case
alay = "aKu KeCe AbieeZzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan  dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower)) # hasilnya bool
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper)) # hasilnya bool

# isalpha() <-- untuk mengecek semua huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cel_judul = judul.istitle() # hasilnya bool
print(judul + " is title = " + str(cel_judul))

## ngecek komponen startswith() endwith() endswith() <-- keren

cek_start = "Sangjanim Oppa".startswith("Sangjanim")
print("start = " + str(cek_start))

cek_end = "Sangjanim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
print(5*"=" + "data" + "="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip("-") # menghilangkan tanda -
print("'"+tengah+"'")





