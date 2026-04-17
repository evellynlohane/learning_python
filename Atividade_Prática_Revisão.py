num = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

divisao = num // num2

print(f'{num} / {num2} = {divisao}')


#########
print('            ')

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

while True:
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print('Os valores não formam um triângulo.')
        break
    else: 
        if a == b and b != c and a != c:
            print(f'O triangulo é isósceles')
        elif c == b and a != c and b != a:
            print(f'O triangulo é isósceles')
        elif c == a and a != b and b != c:
            print(f'O triangulo é isósceles')
        elif c == b and c == a and b == a:
            print(f'O triangulo é equilátero')
        else:
            print(f'O triangulo é escaleno')
        
        break
########
print('            ')

num = int(input('Digite um numero:'))

if num % 2 == 0:

     print(f'Par: {num}') 

else: 

     print(f'Impar: {num}')
   

print('Fim')

########
print('            ')

num = int(input('Digite o numero para a tabuada:'))

for i in range (0,11,1):
    print(f'{num} x {i} = {num * i}')

########
print('            ')

for i in range (0,11,-1):
    print(f'{i}')


