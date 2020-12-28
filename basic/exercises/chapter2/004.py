"""Reproduza em um programa todos os casos de operações aritméticas
do Quadro 2.1, para A = 14 e B = 5, e compare os valores obtidos por
você com os valores esperados constantes do quadro."""


print()
print("Iniciando o Script...")
print("Atribuindo os valores...")
A = 14
B = 5
print()
print("|-------------------------------------------------------------------------|")
print("|  Operação         |   Operador   |    Exemplo    |   Resultado esperado |")
print("|  Adição           |      +       |   C = A + B   |         {0}           |".format(A+B))
print("|  Subtração        |      –       |   C = A – B   |          {0}           |".format(A-B))
print("|  Multiplicação    |      *       |   C = A * B   |         {0}           |".format(A*B))
print("|  Divisão          |      /       |   C = A / B   |        {0}           |".format(A/B))
print("|  Divisão inteira  |     //       |   C = A // B  |          {0}           |".format(A//B))
print("|  Resto (módulo)   |      %       |   C = A % B   |          {0}           |".format(A%B))
print("|  – unário         |      –       |   C = – A     |        {0}           |".format(-A))
print("|  Potenciação      |     **       |   C = A ** B  |     {0}           |".format(A**B))
print("|-------------------------------------------------------------------------|")
print()
print("Encerrando o script...")