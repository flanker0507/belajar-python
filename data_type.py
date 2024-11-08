data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

data_string = "Dilla Jelek"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data : boolean
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))


# konversi tipe data (CASTING TIPE DATA)
# Tipe Data = int, float, str, bool

print("Casting Tipe Data")

data_int = 9
print("data : ", data_int, "Type Data : ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data : ", data_float, "Type Data : ", type(data_float))
print("data : ", data_str, "Type Data : ", type(data_str))
print("data : ", data_bool, "Type Data : ", type(data_bool))


