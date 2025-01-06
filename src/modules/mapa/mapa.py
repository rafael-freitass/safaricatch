import WConio2 as wc
import cursor
import random

VAZIO = " "
PAREDE = "#"
NAVEGAVEL = "."
MATO = "M"
JOGADOR = "@"

maxI = 10  # Altura
maxJ = 20  # Largura
jogadorI, jogadorJ = 1, 1

CHANCE_POKEMON = 0.3

matriz = []

def inicializar_matriz():
    for i in range(maxI):
        linha = []
        for j in range(maxJ):
            if i == 0 or i == maxI - 1 or j == 0 or j == maxJ - 1:
                linha.append(PAREDE)  
            elif random.random() < 0.15:
                linha.append(MATO)  
            else:
                linha.append(NAVEGAVEL)  
        matriz.append(linha)

def desenhar_tela():
    wc.gotoxy(0, 0)
    for i in range(maxI):
        for j in range(maxJ):
            if i == jogadorI and j == jogadorJ:
                wc.textcolor(wc.RED)  # Cor do jogador
                wc.putch(JOGADOR)
            elif matriz[i][j] == PAREDE:
                wc.textcolor(wc.DARKGRAY)  # Cor das paredes
                wc.putch(PAREDE)
            elif matriz[i][j] == NAVEGAVEL:
                wc.textcolor(wc.BROWN)  # Cor das áreas navegáveis
                wc.putch(NAVEGAVEL)
            elif matriz[i][j] == MATO:
                wc.textcolor(wc.GREEN)  # Cor do mato
                wc.putch(MATO)
        wc.putch("\n")

def movimentar_jogador(dI, dJ):
    global jogadorI, jogadorJ
    novoI, novoJ = jogadorI + dI, jogadorJ + dJ

    if matriz[novoI][novoJ] in [NAVEGAVEL, MATO]:
        jogadorI, jogadorJ = novoI, novoJ
        if matriz[novoI][novoJ] == MATO and random.random() < CHANCE_POKEMON:
            wc.gotoxy(0, maxI + 2)
            wc.textcolor(wc.YELLOW)
            print("Você encontrou um Pokémon! Pressione qualquer tecla para continuar.")
            wc.getch()
            wc.clrscr()


if __name__ == "__main__":
    wc.clrscr()
    cursor.hide()
    inicializar_matriz()

    while True:
        desenhar_tela()

        if wc.kbhit():
            _, key = wc.getch()

            if key == "w":  # move para cima
                movimentar_jogador(-1, 0)
            elif key == "s":  # move para baixo
                movimentar_jogador(1, 0)
            elif key == "a":  # move para esquerda
                movimentar_jogador(0, -1)
            elif key == "d":  # move apra direita
                movimentar_jogador(0, 1)
            elif key == "q":  # sai do jogo
                break
