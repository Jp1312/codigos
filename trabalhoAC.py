#funcoes

def imprimir_matriz(matriz):
    for i, linha in enumerate(matriz):
        print(f"{i+1}  ", end='')
        for elemento in linha:
            print(elemento, end=' ')
        print()
def jogo(n1,n2,subs1,subs2):
    tir = 0;ac = 0;p1 = 0;p2 = 0;
    tab1 = [[0, 0, 0, 0, 0] for _ in range(5)]; tab2 = [[0, 0, 0, 0, 0] for _ in range(5)];

    while p1 < 3 and p2 < 3:
        # Jogador 1
        print(f'Jogador 1: {n1}, pressione ENTER para continuar')
        input()
        print(f"JOGADOR 1: {n1}")
        print(f"Tiros: {tir}   Acertos: {ac}\n")
        print("   1 2 3 4 5")
        print()
        imprimir_matriz(tab1);
        l1 = int(input("Qual linha? : "))
        c1 = int(input("Qual coluna? : "))
        temp = (l1, c1)
        if temp in subs2:
            print("ACERTOU!")
            tir += 1;ac += 1; p1 += 1;
            tab1[l1-1][c1-1] = 'S';

        else:
            print("ERROU!");
            tir += 1;
            tab1[l1-1][c1-1] = 'X';

        if p1 >= 3:
            break

        # Jogador 2
        print("\n" * 8);
        print(f'Jogador 2: {n2}, pressione ENTER para continuar')
        input()
        print(f"JOGADOR 2: {n2}")
        print(f"Tiros: {tir}   Acertos: {ac}\n")
        print("   1 2 3 4 5")
        print()
        imprimir_matriz(tab2);
        l2 = int(input("Qual linha? : "))
        c2 = int(input("Qual coluna? : "))
        temp = (l2, c2)
        if temp in subs1:
            print("ACERTOU!")
            tir += 1;ac += 1;p2 += 1
            tab2[l1-1][c1-1] = 'S'
        else:
            print("ERROU!")
            tir += 1
            tab2[l1-1][c1-1] = 'X'

        if p2 >= 3:
            break

    if p1 >= 3:
        print(f"{n1} venceu o jogo!")
    else:
        print(f"{n2} venceu o jogo!")
#bloco principal
subs1 = []
subs2= []

n1 = input("Nome do jogador 1: ")
print("\n")

for c in range(3):
    print(f'submarino {c+1}:\n')

    while True:
        lin = int(input("Linha:"))
        col = int(input(f"Coluna:"))

        if lin < 1 or lin > 5 or col < 1 or col > 5:
            print("\nLinha e coluna devem estar entre 1 e 5. Tente novamente.\n")
        else:
            break

    tup=(lin,col)   #tupla com as coordenadas do submarino
    subs1.append(tup);
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


    tup = (lin, col)
    subs2.append(tup);
    print('\n')


jogo(n1,n2,subs1,subs2)









