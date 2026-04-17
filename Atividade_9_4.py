for num in range (0,101,2):
        print(num)

###########
print('                ')

num = int(input('Digite um numero (0 para sair):'))

while num != 0:
    if num % 2 == 0:
         print(f'Par: {num}') 
    else: 
          print(f'Impar: {num}')
    num = int(input('Digite um numero (0 para sair):'))

print('Fim')
        
###########
print('                ')

for idade in range (0,11,1):
    print('Insira 10 idades: ')
    idade = int(input('Digite uma idade (-1 para sair):'))
    if idade > 17:
        print(f'Maior de idade: {idade}')
    else:
        print(f'Menor de idade: {idade}')
    
###########
print('                ')


