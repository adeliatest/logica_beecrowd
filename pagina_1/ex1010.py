# compra de 2 itens

valor = 0

for i in range(1, 3):
    codigo = int(input(f'Código do item {i}: '))
    qtd_itens = int(input(f'Quantidade do item {i}: '))
    valor_item = float(input(f'Valor do item {i}: R$'))

    # valor = valor + (quantidade * valor do item)
    valor += qtd_itens * valor_item

print(f'O valor total da compra é de: R${valor:.2f}')


