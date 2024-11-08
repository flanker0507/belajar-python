# width and Multiline

# Data

data_name = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = (f"name = {data_name}, umur = {data_umur}, data_tinggi = {data_tinggi}, data nomor sepatu {data_nomor_sepatu}")
print(5*"="+"Data String"+5*"=")
print(data_string)

# string Multiline (dengan mengunakan enter, newline \n)
data_string = (f"name = {data_name}, \numur = {data_umur}, \ndata_tinggi = {data_tinggi}, \ndata nomor sepatu {data_nomor_sepatu}")
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string Multiline (kutip triplets)

data_string = f"""name = {data_name}
umur = {data_umur}
data tinggi = {data_tinggi}
data nomor sepatu = {data_nomor_sepatu}

"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_name = "ucup"
data_string = f"""
name   = {data_name:>5}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}

"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
