n = int(input())

p = []

for i in range(n):
    x = int(input())
    if x:
        p.append(x)
    else:
        p.pop()
print(sum(p))