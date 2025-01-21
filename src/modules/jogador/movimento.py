# Importações de biblioteca
import random
import WConio2 as wc
import os
import sys

# Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))

## Adiciona caminho para 'jogador' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'mapa')))

# Importações do projeto
from text_functions import *
from elementos_mapa import *

# Globais
_maxI_ = 20 
_maxJ_ = 20  
_pos_xy_jogador_ = [1, 1]

CHANCE_POKEMON = 0.3

matriz = []

# Retorna True se o elemento no mapa for passável, False se não for passável
def verificar_colisao(mapa_atual: list, pos_x: int, pos_y: int):
    elementos = elementos_ASCII()
    elemento_alvo = mapa_atual[pos_y][pos_x]

    # Itera a lista de elementos
    for i in range(len(elementos)):
        # Verifica se o char é único ou é um set
        if (type(elementos[i]) == str):
            # Compara o elemento alvo e char e verifica seé passável
            if (elemento_alvo == elementos[i].get('char')):
                if (elementos[i].get('passa')):
                    return True
                break
        else:
            for j in range(len(elementos[i].get('char'))):
                if (elemento_alvo == elementos[i].get('char')[j]):
                    if (elementos[i].get('passa')):
                        return True
                    else:
                        return False
                    
    return False

# Movimentação literal, de um em um
def movimentar_jogador(mapa, dI, dJ):
    global _pos_xy_jogador_
    novo_x = _pos_xy_jogador_[0] + dI
    novo_y = _pos_xy_jogador_[1] + dJ

    if verificar_colisao(mapa, novo_x, novo_y):
        wc.gotoxy(_pos_xy_jogador_[0], _pos_xy_jogador_[1])
        imprimir_elemento_bc(mapa[_pos_xy_jogador_[0]][_pos_xy_jogador_[1]])
        _pos_xy_jogador_[0] = novo_x 
        _pos_xy_jogador_[1] = novo_y
        wc.gotoxy(_pos_xy_jogador_[0], _pos_xy_jogador_[1])
        imprimir_elemento_bn('jogador')
        #if matriz[novo_x][novo_y] == MATO and random.random() < CHANCE_POKEMON:
        #    wc.gotoxy(0, _maxI_ + 2)
        #    wc.textcolor(wc.YELLOW)
        #    print("Você encontrou um Pokémon! Pressione qualquer tecla para continuar.")
        #    wc.getch()
        #    wc.clrscr()

# Atualiza visualização e posição do jogador seguindo coordenada 4d
def teleporte(mapa:list, coordenada_1:list, coordenada_2:list):
    # usa o primeiro par para identificar se está numa matriz sendo exibida 
    # e segundo par para verificar posição do jogador é igual ao ponto de teleporte
    if ((coordenada_1[0][1] == True) and (_pos_xy_jogador_ == coordenada1[2][3])):
        if not(coordenada_1[0][1] == coordenada_2[0][1]):
            att_container(mapa, coordenada_2[0])
        _pos_xy_jogador_ = coordenada_2[2][3]
    elif((coordenada_2[0][1] == True) and (_pos_xy_jogador_ == coordenada2[2][3])):
        if not(coordenada_2[0][1] == coordenada_1[0][1]):
            att_container(mapa, coordenada_1[0])
        _pos_xy_jogador_ = coordenada_1[2][3]

# Altera a global de posição e imprime jogador na posição passada
def origem_jogador(coord_x: int, coord_y: int, direcao = 0, borda_tela = 2):
    global _pos_xy_jogador_

    wc.gotoxy(coord_x + borda_tela, coord_y + borda_tela)
    imprimir_elemento_bn('jogador', 15, direcao)
    _pos_xy_jogador_[0] = coord_x
    _pos_xy_jogador_[1] = coord_y
    wc.gotoxy(0, 30)    

# Exibe, reimprime e capta entrada do usuário
def rodar():
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
