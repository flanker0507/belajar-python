'''Module matematika'''

def tambah(*args):
    result = 0
    for i in args:
        result += i
        return result

def kali(*args):
    result = 1
    for i in args:
        result += i
        return result

def pangkat(n):
    return lambda angka:angka**n