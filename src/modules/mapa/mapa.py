# Importações de bibliotecas
import WConio2 as wc
#import cursor
import os
import sys
from time import sleep

# Adição de caminhos
## Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))

## Adiciona caminho para 'jogador' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'jogador')))

# Importações do projeto
from elementos_mapa import *
from text_functions import *
from movimento import *

# Retorna o mapa como uma lista de matrizes do tamanho da tela
def carregar_mapa(nome_arquivo_mapa):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), nome_arquivo_mapa))) as arquivo:
        mapa = arquivo.read().split('\n')
        return (divide_content(mapa, True))
        
# Retorna coordenadas de todas ocorrências de portal no mapa
def encontrar_coord_portais(mapa: list):
    elementos = elementos_ASCII() 

    # Busca char definido como portal
    for i in range(len(elementos)):
        if (elementos[i].get('nome') == 'portal'):
                portal = elementos[i].get('char')
                break

    coordenadas = []

    # Itera lista de matrizes
    for i in range(len(mapa)):
        # Itera cada matriz
        for j in range(len(mapa[i][1])):
            # Itera cada linha
            for k in range(len(mapa[i][1][j])):
                if (mapa[i][1][j][k] == portal):
                    coordenadas.append([i, 1, j, k])

    return coordenadas    

# Geração de mapa aleatorio
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


# APENAS PARRA TESTE
def segundo_Para_Minuto(number):
    return number

get_NumValue = 180

# Tela do mapa deve conter: borda de 2 linhas
# Fora da borda: título do jogo, timer
# Dentro da borda: parte do mapa que está sendo exibida
def main():
#    while (timer_Main and zerar_Timer)
    wc.clrscr()
    wc.setcursortype(0)
    # Impressão padrão
    ## Impressão fora a margem
    titulo = 'SafariCatch'
    alinhar_centro(titulo, 0)
    print(titulo)
    tempo = '{}'.format(180)
    alinhar_direita(tempo, 1)
    print(tempo)

    ## Impressão dentro da margem
    alinhar_add_margem_tela(2)
    mapa = carregar_mapa('mapa.txt')

    # Impressão específica DESSE mapa
    att_container(mapa, 4)
    impressao_matriz_m(mapa, True, 2)
    origem_jogador(11, 3, 2)
    sleep(0.4)
    impressao_matriz_m(mapa, True, 2)
    origem_jogador(11, 4, 2)
    sleep(0.4)
    impressao_matriz_m(mapa, True, 2)
    origem_jogador(11, 5, 2)

    # Iniciar timer e movimento
    ## mover
    segundo_Para_Minuto(get_NumValue)
    ## movimento
    while(True):
        if wc.kbhit():
            _, key = wc.getch()

            if key == "w":  # move para cima
                movimentar_jogador(mapa[4][1], -1, 0)
            elif key == "s":  # move para baixo
                movimentar_jogador(mapa[4][1], 1, 0)
            elif key == "a":  # move para esquerda
                movimentar_jogador(mapa[4][1], 0, -1)
            elif key == "d":  # move apra direita
                movimentar_jogador(mapa[4][1], 0, 1)
            elif key == "q":  # sai do jogo
                break
    
    ## A partir daqui precisa ser mutável/estar no laço

    pass


main()
#if __name__ == "__main__":
#    wc.clrscr()
#    cursor.hide()
#    inicializar_matriz()
#    while True:
#        desenhar_tela()
#        if wc.kbhit():
#            _, key = wc.getch()
#            if key == "w":  # move para cima
#                movimentar_jogador(-1, 0)
#            elif key == "s":  # move para baixo
#                movimentar_jogador(1, 0)
#            elif key == "a":  # move para esquerda
#                movimentar_jogador(0, -1)
#            elif key == "d":  # move apra direita
#                movimentar_jogador(0, 1)
#            elif key == "q":  # sai do jogo
#                break