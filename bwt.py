print("----------- Burrows-Wheeler's algorithm -----------")
string = input ("Insert a word:  ")
print("---- added $ ----")
string+="$"
print(string)
spins = []
for i in range(le(string)):
    spins.append(string[i:] + string[:i])
    print(spins)