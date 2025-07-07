# salário com bônus

nome = 'Lucas'
salario = 500.00
vendas_feitas = 1230.30
comissao_por_venda = 0.15

bonus = vendas_feitas * comissao_por_venda
salario_com_bonus = bonus + salario

print(f'Total a receber: {round(salario_com_bonus, 2)}')