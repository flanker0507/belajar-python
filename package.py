import sians.matematika
from sians import fisika 
from sians.fisika import gaya as force

result = sians.matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah dari package adalah = {result}")

result = sians.matematika.kali(1,2,3,4,5)
print(f"Hasil tambah dari package adalah = {result}")

pangkat1 = sians.matematika.pangkat(2)
print(f"Hasil Pangkat Dari Package = {pangkat1(5)}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")
