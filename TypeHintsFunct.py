''' Type hints untuk Function'''

# bentuk standar fungsi yang udah kita pelajari

'''
studi kasus
def fungsi(parameneter):
    hasil = paramenet**2
    print(hasil)
    
    
fungsi(1)
fungsi(ucup)
fungsi(True)
'''

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) ->int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(9)
print(HASIL)

def display(argument:string):
    print(argument)

display("Dilla")