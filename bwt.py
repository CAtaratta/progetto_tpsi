print("----------- Burrows-Wheeler's algorithm -----------")
string = input ("Insert a word:  ")
print("---- added $ ----")
string+="$"
print(string)
spins = []
for i in range(len(string)):
    spins.append(string[i:] + string[:i])

print("---- turnovers ----")
for s in spins:
    print(s)


