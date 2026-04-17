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

print('Insira 10 idades: ')

for idade in range (0,11,1):
    print('                ') #Utilizei por estética
    idade = int(input('Digite uma idade:'))
    if idade > 17:
        print(f'Maior de idade: {idade}')
    else:
        print(f'Menor de idade: {idade}')
    
###########
print('                ')

print('Insira 30 idades: ')
print('                ') #Utilizei por estética

for nota in range (0,31,1):
    print('                ') #Utilizei por estética
    nota = int(input('Digite uma nota para portugês:'))
    if nota >= 7:
        print(f'Aprovado: {nota}')
    elif nota < 7 and nota >= 5:
        print(f'Em recuperação: {nota}')
    else:
        print(f'Reprovado: {nota}')