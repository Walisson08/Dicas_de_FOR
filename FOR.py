i = int(input('inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('fim')

s = 0
for c in range (0, 5):
    n = int(input('Digite um  valor:'))
    s += n 
print(f'O somatorio de todos os valores foi {s}')
