"""
Escreva um programa que calcule o faturamento de um representante
comercial que recebe R$ 500,00 fixos e 6% de comissão sobre as
vendas do mês. 
Considere que ele fechou o mês com um valor de R$12.398,00 
em vendas. Exiba o resultado com duas casas decimais.
"""
print()
print("Inicio do Programa")
print("")
fixo = 500.00
##vendas = 12398.00
vendas = float(input("Digite o valor de vendas: "))
print()
comissao = 6 / 100
fat = fixo + vendas * comissao
print("Faturamento do mes = {0:.2f}".format(fat))
print("")
print("Fim do Programa")
print()