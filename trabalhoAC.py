#funcoes
def desenhatabuleiro(n1):
    tir = 0;
    ac = 0;
    print(f"JOGADOR 1  :   {n1}\n")
    print(f"Tiros:  {tir}   Acertos: {ac}   \n")
    print("   1  2  3  4  5")
    for x in range(5):  #
        print(x + 1, end=": ")
        for c in range(5):
            print(0,end="  ")
        print("\n")




#bloco principal
subs1 = []
subs2= []

n1 = input("Nome do jogador 1: ")
print("\n")

for c in range(3):
    print(f'SUBMARINO {c+1} \n')

    while True:
        lin = int(input(f"Linha (1 a 5): "))
        col = int(input(f"Coluna (1 a 5): "))

        if lin < 1 or lin > 5 or col < 1 or col > 5:
            print("\nLinha e coluna devem estar entre 1 e 5. Tente novamente.\n")
        else:
            break

    subs1.append((lin, col))
    print('\n')

    subs1.append((lin, col))
    print('\n')

print('\n' * 10)

n2 = input("Nome do jogador 2: ")
print("\n")

for c in range(3):
    print(f'SUBMARINO {c+1} \n')

    while True:
        lin = int(input(f"Linha (0 a 5): "))
        col = int(input(f"Coluna (0 a 5): "))

        if lin < 1 or lin > 5 or col < 1 or col > 5:
            print("\nOs números de linha e coluna devem estar entre 1 e 5. Tente novamente.\n")
        else:
            break

    subs2.append((lin, col))
    print('\n')

print(f'Jogador 1: {n1}, pressione ENTER para continuar')
input()

print('\n' * 10)

#desenhando o quadrado



desenhatabuleiro(n1)

