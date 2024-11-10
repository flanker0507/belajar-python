data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Hallo, apa kabar ?"')
print("'Hallo, apa kabar ?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day isn\'t it?')

# backslash
print("C:\\user\\Dilla")

# tab
print("ucup\t\t\tOtong, semakin jauh")

#backspace
print("ucup \botong, jadi deketan")

# newLine
print("baris pertama. \nBaris Kedua.") # LF -> Line Feef
print("baris pertama. \rBaris Kedua.") # CR -> Carriage Return
print("baris pertama. \r\nBaris Kedua.") #CRLF -> Line Feed Carriage Return

# 3. Sring Literal atau raw

# hati-hati
print('C:\new Folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new Folder')

# multiple literal string
print("""
Name : Ucup
Kelas : 3 SD
""")

# multiline literal string and RAW
print(r"""
Name : Ucup
Kelas : 3 SD
Website : www.ucup.com\newID
""")
