n = int(input())

amigos = []
tempos = {}
esperando = {}

def atualiza(n = 1):
    for i in amigos:
        i = str(i)
        if esperando[i] == 1:
            tempos[i]+=n

for i in range(n):
    r, a = input().split()
    if r != 'T':
        if int(a) not in amigos:
            amigos.append(int(a))
            tempos[a] = 0
            esperando[a] = 1
        if r == 'E':
            esperando[a] = 0
        else:
            esperando[a] = 1
        atualiza()
    else:
        atualiza(int(a))
        if i < n-1:
            atualiza(-1)
amigos.sort()
for i in amigos:
    i = str(i)
    if esperando[i]:
        tempos[i] = -1
    print(i, tempos[i])