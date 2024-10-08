# Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e remova todos os elementos duplicados, mantendo a
# ordem original dos elementos. Ao final, apresente os valores fornecidos
# pelo usuário e o resultado do processamento da sua solução;

# Lê a entrada do usuário
entrada = input("Digite uma lista de números inteiros, separados por espaço: ")

# Converte a entrada em uma lista de números inteiros
numeros = []
for num in entrada.split():
    try:
        numeros.append(int(num))  # Tenta converter cada entrada para inteiro
    except ValueError:
        print(f"'{num}' não é um número inteiro válido e será ignorado.")

# Inicializa uma lista para números únicos
numeros_unicos = []
vistos = set()

# Encontra números únicos
for numero in numeros:
    if numero not in vistos:
        vistos.add(numero)
        numeros_unicos.append(numero)

# Exibe as listas
print("Lista original:", numeros)
print("Lista sem duplicatas:", numeros_unicos)

# 2. Escreva um programa que leia uma lista de números inteiros fornecida
# pelo usuário e um número alvo. O programa deve encontrar todos os
# pares de números na lista cuja soma seja igual ao número alvo.
# 1. Exemplo: Digite os números separados por espaço: 2 4 3 5 7

numeros = []
entrada = input("Digite os números inteiros (pressione Enter para finalizar): ")

while entrada:
    numeros.append(int(entrada))
    entrada = input("Digite o próximo número (ou pressione Enter para finalizar): ")

alvo = int(input("Digite o número alvo: "))

pares_encontrados = []
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] + numeros[j] == alvo:
            pares_encontrados.append((numeros[i], numeros[j]))

if pares_encontrados:
    print("Pares encontrados que somam ao número alvo:")
    for par in pares_encontrados:
        print(par)
else:
    print("Nenhum par encontrado que some ao número alvo.")

# 3. Escreva um programa que leia uma lista de números inteiros fornecida pelo
# usuário e um número de passos. O programa deve rotacionar a lista para a
# direita pelo número de passos especificado.
# Exemplo: Digite os números separados por espaço: 1 2 3 4 5

# Digite o número de passos: 2
# Lista rotacionada: [4, 5, 1, 2, 3]

numeros = []
entrada = input("Digite os números inteiros (pressione Enter para finalizar): ")

while entrada:
    numeros.append(int(entrada))
    entrada = input("Digite o próximo número (ou pressione Enter para finalizar): ")

passos = int(input("Digite o número de passos: "))

n = len(numeros)
passos = passos % n 

numeros_rotacionados = numeros[-passos:] + numeros[:-passos]

print("Lista rotacionada:", numeros_rotacionados)

# 4. Escreva um programa que leia uma lista de números inteiros fornecida pelo
# usuário e utilize uma list comprehension para gerar uma nova lista contendo
# os quadrados de todos os números ímpares da lista original.
# Exemplo: Digite os números separados por espaço: 1 2 3 4 5 6 7 8 9 10

# Quadrados dos números ímpares: [1, 9, 25, 49, 81]

numeros = []
entrada = input("Digite os números inteiros (pressione Enter para finalizar): ")

while entrada:
    numeros += [int(entrada)]
    entrada = input("Digite o próximo número (ou pressione Enter para finalizar): ")

quadrados_impares = [num ** 2 for num in numeros if num % 2 != 0]

print("Quadrados dos números ímpares:", quadrados_impares)