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


print('Insira as notas de português: ')
print('                ') # Utilizei por estética


somam = 0  
somaf = 0  
somao = 0  


for i in range(10): 
    print('                ') 
    nome = str(input('Digite o nome do aluno: '))
    genero = str(input("Digite o gênero (M, F ou Outro): ")).upper()
    nota = float(input('Digite uma nota para português: '))

    
    if nota >= 7:
        print('Aprovado: ' + str(nota))
    elif nota < 7 and nota >= 5:
        print('Em recuperação: ' + str(nota))
    else:
        print('Reprovado: ' + str(nota))

    
    match genero:
        case "M":
            print("Masculino")
            somam += 1
        case "F":
            print("Feminino")
            somaf += 1
        case "OUTRO":
            print("Outro")
            somao += 1
        case _:
            print("Entrada inválida para gênero")

print('                ') # Utilizei por estética
print('Total feminino: ' + str(somaf))
print('                ') # Utilizei por estética
print('Total Masculino: ' + str(somam))
print('                ') # Utilizei por estética
print('Total outro: ' + str(somao))