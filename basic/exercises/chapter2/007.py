"""Escreva a sequência de comandos para calcular o salário bruto de um
profissional que ganha por hora, sabendo que ele ganha R$ 14,25/h e
trabalhou 163 horas normais e 20 horas extras (pagam o dobro)."""

print()
print("Iniciando o Script...")
print("Atribuindo os valores...")
print()
valor_hora = 14.25
horas_trabalhadas = 163
horas_extras = 20

total_a_receber = (horas_trabalhadas * valor_hora) + (horas_extras *(valor_hora*2))

print("valor_hora <= {0}".format(valor_hora))
print("horas_trabalhadas <= {0}".format(horas_trabalhadas))
print("horas_extras <= {0}".format(horas_extras))
print()

print("Total a receber: {0}".format(total_a_receber))
print()
print("Encerrando o script...")
print()