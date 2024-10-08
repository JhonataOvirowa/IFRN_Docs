#tuplas:
# 1. Escreva um programa que receba uma tupla de números inteiros e como
# saída uma nova tupla com os elementos pares da tupla original. Por
# exemplo, se a tupla for (1, 2, 3, 4, 5), o programa deve imprimir (2, 4).

tupla_original = (1, 2, 3, 4, 5)
tupla_pares = ()

for numero in tupla_original:
    if numero % 2 == 0:
        tupla_pares += (numero,)

print(tupla_pares)

# 2. Escreva um programa que receba uma tupla de strings e exiba uma nova
# tupla com as strings ordenadas alfabeticamente e sem repetições. Por
# exemplo, se a tupla for ("banana", "maçã", "laranja", "banana", "uva"), o
# programa deve imprimir ("banana", "laranja", "maçã", "uva").

tupla_original = ("banana", "maçã", "laranja", "banana", "uva")
tupla_unica = set(tupla_original)
tupla_ordenada = tuple(sorted(tupla_unica))

print(tupla_ordenada)

# Dicionários:
# 3. Escreva um programa que receba um dicionário que mapeia nomes de
# países para suas populações e exiba o nome do país com a maior
# população. Por exemplo, se o dicionário for {"Brasil": 211.8, "China":
# 1400.5, "Índia": 1366.4}, o programa deve exibir "China".

dicionario_paises = {"Brasil": 211.8, "China": 1400.5, "Índia": 1366.4}

maior_pais = ""
maior_populacao = 0

for pais, populacao in dicionario_paises.items():
    if populacao > maior_populacao:
        maior_populacao = populacao
        maior_pais = pais

print(maior_pais)

# 4. Escreva um programa que receba como entrada um dicionário que mapeia
# nomes de alunos para suas notas e exiba um novo dicionário com os nomes
# dos alunos aprovados e suas respectivas médias. Considere que um aluno é
# aprovado se sua média for maior ou igual a 7. Por exemplo, se o dicionário
# for {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]},
# o programa deve exibir {"Ana": 8.33, "Carla": 8.0}.

notas_alunos = {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]}
alunos_aprovados = {} 

for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)

    if media >= 7:
        alunos_aprovados[aluno] = round(media, 2)
print(alunos_aprovados)

# Conjuntos:
# 5. Escreva um programa que receba dois conjuntos de números inteiros como
# entrada e exiba um novo conjunto com os elementos que estão em ambos
# os conjuntos. Por exemplo, se os conjuntos forem {1, 2, 3, 4} e {3, 4, 5, 6},
# o programa deve exibir {3, 4}.

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}  

conjunto_comum = set()  
for numero in conjunto1:
    if numero in conjunto2:
        conjunto_comum.add(numero) 

print(conjunto_comum)

# 6. Escreva um programa que receba um conjunto de strings e exiba um novo
# conjunto com as strings que são palíndromos. Um palíndromo é uma palavra
# que é igual a ela mesma quando lida de trás para frente. Por exemplo, se o
# conjunto for {"arara", "casa", "ovo", "radar"}, o programa deve exibir
# {"arara", "ovo", "radar"}.

conjunto_strings = {"arara", "casa", "ovo", "radar"} 
conjunto_palindromos = set()

for palavra in conjunto_strings:
    if palavra == palavra[::-1]:
        conjunto_palindromos.add(palavra)  

print(conjunto_palindromos)