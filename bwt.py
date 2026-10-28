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

n = len(spins)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if spins[j] > spins[j + 1]:
            temp = spins[j]
            spins[j] = spins[j + 1]
            spins[j + 1] = temp

print("---- turnovers rearranged ----")
for s in spins:
    print(s)

bwt = ""
for s in spins:
    bwt += s[-1]

print("---- BWT ----")
print(bwt)