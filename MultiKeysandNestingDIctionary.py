from datetime import datetime

mahasiswa1 = {
    'name':'Ucup Surucup',
    'nim' : '19143769',
    'sks_lulus' : 144,
    'beasiswa' : False,
    'lahir' : datetime(2001, 4, 10)
}

mahasiswa2 = {
    'name':'Otong Surotong',
    'nim' : '19143767',
    'sks_lulus' : 140,
    'beasiswa' : True,
    'lahir' : datetime(2005, 12, 12)
}

mahasiswa3 = {
    'name':'Asep SI kasep',
    'nim' : '19143769',
    'sks_lulus' : 144,
    'beasiswa' : False,
    'lahir' : datetime(2001, 1, 1)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3,
}

print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<9} {'SKS':<9} {'BEASISWA':<9} {'LAHIR':<10}")
print(f"-"*60)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['name']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {NIM:<4} {SKS:<9} {BEASISWA:^9} {LAHIR:<10}")


