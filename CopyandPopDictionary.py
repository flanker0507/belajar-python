# Copy
teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep kasep",
    "cuy" : "ucuy surucuy"
}

friends = teman_teman.copy()

friends.update({"cup": "ucup kecup"})
print(f"teman - teman = {teman_teman}\n")
print(f"friends = {friends}\n")

# Pop (berdasarkan Key)
dataAsep = friends.pop("sep")
print(f"Data Asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# Popitem (yang terakhir aja)
data_terakhir = friends.popitem()
print(f"data terakhir = {data_terakhir}\n")
print(f"friends = {friends}")