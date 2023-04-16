#Atividade 02 : Ler cinco valores inteiros e apresentar o maior e o menor valor informado.

# var , tipo , função , oque irá aparecer ao usuário.

a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))
d = int(input('Digite o quarto número:'))
e = int(input('Digite o quinto número:'))

# Lógica para checar o menor número digitado.

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if d < b and d < c:
    menor = d
if e < c and e < d:
    meno = e
print('O menor valor digitado foi {}'.format(menor))

# Lógica para checar o maior número digitado.

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if d > b and d > c:
    maior = d
if e > c and e > d:
    maior = e
print('O maior valor digitado foi {}'.format(maior))

# Caso tente usar vírgula o programa não compilar devido suas variáveis ta definida como números inteiros.
