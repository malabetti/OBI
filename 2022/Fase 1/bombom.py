x = input(); nd = x[1]

plu = 0; ped = 0

valores = {
    'A':10,
    'J':11,
    'Q':12,
    'K':13
}

for i in range(3):
    x = input()
    if x[1] != nd:
        plu += valores[x[0]]
    else:
        plu += valores[x[0]] + 4

for i in range(3):
    x = input()
    if x[1] != nd:
        ped += valores[x[0]]
    else:
        ped += valores[x[0]] + 4

if ped > plu:
    print('Edu')
elif plu > ped:
    print('Luana')
else:
    print('empate')