# list -> array, mengakses menggunakan index
data_list = ['Yuda', 'Wira', 'Pratama']

print(data_list[0])

# dictionary (dict) -> associative array
# identifier - key

data_dict = {
    'key':'value',
    'yd': 'Yuda',
    'wr' : 'Wira',
    'pr' : 'Pratama',
    'dl' : data_list

}

print(f"Data Dict = {data_dict['dl']}")

# Operator Dictionary

# Panjang Dictionary
LENDICT = len(data_list)
print(f"Panjang Dictionary = {LENDICT}")

# Mencari Dictionary
KEY = "pr"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data dict = {CHECKKEY}")
KEY = "ad"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data dict = {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict.get("yd"))
print(data_dict.get("dd", "key tidak di temukan"))

# mengupdate data
data_dict.update({"yd":"Yuda Ganteng Banget"})
print(data_dict)
data_dict.update({"dd":"dillaa"})
print(data_dict)

# delete
del data_dict["dl"]
print(data_dict)

