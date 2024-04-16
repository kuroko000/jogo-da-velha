def novoTabuleiro():
    return [0,0,0,
            0,0,0,
            0,0,0]

def imprimirTabuleiro(tabuleiro):
    for indice, valor in enumerate(tabuleiro):
        if valor == 0:
            print (" ", indice + 1, sep = "", end = '')
        elif valor == 1:
            print (" x", end = '')
        else:
            print(" o", end = '')

        if indice == 2 or indice == 5:
            print ("\n---+---+---\n", end = '')
        elif indice < 8:
            print(" |", end='')
    print("\n")

    def recebeJogada(jogador):
        try:
            jogado = int(input("Digite a posição a jogar 1-9 (jogador %s):"% jogador))
            return jogada
        except ValueError:
            print("entrada invalida")
            return -1
        
def posicaoValida (jogada, tabuleiro):
    if jogada < 1 or jogada >9:
        print ("Posição invalida")
        return False
    if tabuleiro[jogada - 1] != 0:
        print ("posição ocupada")
        return False
    return True


def mudaJogador (jogador, jogada, tabuleiro):
    if jogador == "x":
        tabuleiro[jogada - 1] = 1
        return "o"
    
    else:
        tabuleiro[jogada - 1] = 2
        return "x"
    
def verificaFimDeJogo(numJogadas, tabuleiro):
    #verifica linhas
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]: #
        if tabuleiro [0] == 1:
            print ("Jogador x ganhou")
            return 1
        elif tabuleiro[0] == 2:
            print ("Jogador o ganhou")
            return
    if tabuleiro[3] == tabuleiro [4] == tabuleiro [5]:
        if tabuleiro [3] == 1:
            print("Jogador x ganhou")
            return 1
        elif tabuleiro [3] == 2:
            print ("Jogador o ganhou")
            return 2
    if tabuleiro [6] == tabuleiro[7] == tabuleiro[8]:
        if tabuleiro[6] == 1:
            print("Jogador x ganhou")
            return 1
        elif tabuleiro[6] == 2:
            print("Jogador o ganhou")
            return 2
            #verificar colunas
    if tabuleiro [0] == tabuleiro [3] == tabuleiro [6]:
        if tabuleiro[0] == 1:
            print("Jogador x ganhou")
            return
        elif tabuleiro[0] == 2:
            print ("Jogador o ganhou")
            return 2
    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        if