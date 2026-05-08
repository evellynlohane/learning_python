valor = float(input('Digite o valor da compra: R$ '))

if valor > 100:
    desconto = valor * 0.1
    print (f'Desconto de 10%: {desconto}')
    valor_com_desconto = valor * 0.9 #pois o desconto é 10%, mas o valor final será 90% do valor inicial
    print(f'Sua compra ficou com desconto de 10%: {valor_com_desconto:.2f}')
else:
    print(f'Sua compra ficou: {valor}')

