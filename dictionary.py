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