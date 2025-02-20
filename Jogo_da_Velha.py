tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
tabuleiro_demonstrativo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Jogo_rodando = True
i = 0
j = 0
def ganhou(i, j):
    global Jogo_rodando
    if tabuleiro[i][j] == 'x':
        print("o jogador 1 ganhou!")
        Jogo_rodando = False
    elif tabuleiro[i][j] == 'o':
        print("o jogador 2 ganhou!")
        Jogo_rodando = False
    return ''

def avaliar():
    for num1 in range(0, 2):
        if tabuleiro[0][num1] == tabuleiro[1][num1] and tabuleiro[1][num1] == tabuleiro[2][num1]:
            print(ganhou(0, num1))
        elif tabuleiro[num1][0] == tabuleiro[num1][1] and tabuleiro[num1][1] == tabuleiro[num1][2]:
            print(ganhou(num1, 0))

    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        print(ganhou(0, 0))
    elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
        print(ganhou(0, 2))

def jogar1(posicao):
    print(posicao)
    if posicao == 1:
        tabuleiro[0][0] = 'x'
    elif posicao == 4:
        tabuleiro[1][0] = 'x'
    elif posicao == 7:
        tabuleiro[2][0] = 'x'
    elif posicao == 2:
        tabuleiro[0][1] = 'x'
    elif posicao == 5:
        tabuleiro[1][1] = 'x'
    elif posicao == 8:
        tabuleiro[2][1] = 'x'
    elif posicao == 3:
        tabuleiro[0][2] = 'x'
    elif posicao == 6:
        tabuleiro[1][2] = 'x'
    elif posicao == 9:
        tabuleiro[2][2] = 'x'
    else:
        print('posição não encontrada')


def jogar2(posicao):
    if posicao == 1:
        tabuleiro[0][0] = 'o'
    elif posicao == 4:
        tabuleiro[1][0] = 'o'
    elif posicao == 7:
        tabuleiro[2][0] = 'o'
    elif posicao == 2:
        tabuleiro[0][1] = 'o'
    elif posicao == 5:
        tabuleiro[1][1] = 'o'
    elif posicao == 8:
        tabuleiro[2][1] = 'o'
    elif posicao == 3:
        tabuleiro[0][2] = 'o'
    elif posicao == 6:
        tabuleiro[1][2] = 'o'
    elif posicao == 9:
        tabuleiro[2][2] = 'o'
    else:
        print('posição não encontrada')


for num in tabuleiro_demonstrativo:
    print(num)

quantidade = 0

while Jogo_rodando:

    if quantidade % 2 == 0:
        valor = int(input("jogador 1\nescolha uma posição:"))
        jogar1(valor)
    else:
        valor = int(input("jogador 2:\nescolha uma posição"))
        jogar2(valor)
    quantidade = quantidade + 1
    for num in tabuleiro:
        print(num)
    avaliar()
    if quantidade == 9:
        print("deu zebra")
        break