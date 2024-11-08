a = 10
b = 3

hasil = a + b
print(a, '+', b, '=', hasil)

hasil = a - b
print(a, '-', b, '=', hasil)

hasil = a * b
print(a, '*', b, '=', hasil)

hasil = a / b
print(a, '/', b, '=', hasil)

# OPERASI EKSPONEN (PANGKAT)

hasil = a ** b
print(a, '**', b, '=', hasil)

# modulo
hasil = a % b
print(a, '%', b, '=', hasil)

#floor division
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '%', z, '//', x, '=', hasil)