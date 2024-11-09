# Looping Dictionary

friends = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep kasep",
    "cuy" : "ucuy surucuy"
}

# looping first try (yang keluar hanya key nya)
for friend in friends:
    print(friend)

# operator untuk mengambil item / iterables
keys = friends.keys()
print(keys)

for key in friends.keys():
    print(friends.get(key))

values = friends.values()
print(values)

for i in friends.values():
    print(i)

items = friends.items()
print(items)

for item in friends.items():
    print(item)

for key, value in friends.items():
    print(f"Key = {key}, value = {value}")