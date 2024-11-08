# membuat gabungan area rentang dari angka

# +++++3--------10++++++

inputUser = float(input("masukkan angka yang bernilai kurang dari 3 atau lebih dari 10: "))

# ++++3-----
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari: ",isKurangDari)

# -----10+++++
# memerikas angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari: ",isLebihDari)

# +++++3--------10++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan : ",isCorrect)


#  -------3+++++++10------
# kasus irisan

inputUser = float(input("masukkan angka yang bernilai lebih dari 3 dan kurang dari 10: "))
# ------3++++++++++
isLebihDari = (inputUser > 3)
print("lebih dari 3: ",isLebihDari)

# ++++++10-------
isKurangDari = (inputUser < 10)
print("kurang dari 10: ",isKurangDari)

isInRange = isLebihDari and isKurangDari
print("angka yang anda masukkan : ",isInRange)

# EXERCISE

# 1. -------0++++++5---------8++++++++11-------
inputUser = float(input("masukkan angka kurang dari 5 atau lebih dari 8 dan kurang dari 11: "))
# -------0++++++5---------
isKurangDari5 = (inputUser < 5)
print("kurang dari 5: ",isKurangDari5)

# ---------8++++++++
isLebihDari8 = (inputUser > 8)
print("Lebih dari 8: ",isLebihDari8)

# ++++++++11-------
isKurangDari11 = (inputUser < 11)
print("kurang dari 11: ",isKurangDari11)

isCorrect = isKurangDari5 or isLebihDari8 and isKurangDari11
print("angka yang anda masukkan : ",isCorrect)

# 2. +++++++0------5++++++++++8--------11++++++

inputUser = float(input("masukkan angka lebih dari 5 atau kurang dari 8 dan lebih dari 11: "))
# +++++++0------5++++++++++
isLebihDari5 = (inputUser > 5)
print("lebih dari 5: ",isLebihDari5)

# ++++++++++8--------
isKurangDari8 = (inputUser < 8)
print("Kurang dari 8: ",isKurangDari8)

# --------11++++++
isLebihDari11 = (inputUser > 11)
print("Lebih dari 11: ",isLebihDari11)

isCorrect = isLebihDari5 and isKurangDari8 or isLebihDari11
print("angka yang anda masukkan : ",isCorrect)
