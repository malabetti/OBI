alfabeto = [
    'a','b', 'c', #a
    'd', 'e', 'f', 'g', #e
    'h', 'i', 'j', 'k', 'l', #i
    'm', 'n', 'o', 'p', 'q', 'r', #o
    's', 't', 'u', 'v', 'x', 'z' #u
]
vogais = ['a', 'e', 'i', 'o', 'u']

str1 = input()
str2 = ''

for i in str1:
    #1º letra
    str2 += i
    if i not in vogais:
        #2º letra
        if alfabeto.index(i) < 3:
            str2 += 'a'
        elif alfabeto.index(i) < 7:
            str2 += 'e'
        elif alfabeto.index(i) < 12:
            str2 += 'i'
        elif alfabeto.index(i) < 18:
            str2 += 'o'
        else:
            str2 += 'u'
        #3º letra
        for j in range(alfabeto.index(i)+1, len(alfabeto)):
            if alfabeto[j] not in vogais:
                str2 += alfabeto[j]
                break
        if i == 'z':
            str2 += 'z'
print(str2)