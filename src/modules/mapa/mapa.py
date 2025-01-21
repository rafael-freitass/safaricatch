# mapa.py cria e passa informações da tela de mapa

# Importações de bibliotecas
import os
import sys
import WConio2 as wc
from time import sleep

# Adição de caminhos
## Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))
## Adiciona caminho para 'jogador' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'jogador')))

# Importações do projeto
from map_functions import *
from timer import *
from text_functions import *
from movimento import *


# Tela do mapa deve conter: borda de 2 linhas
# Fora da borda: título do jogo, timer
# Dentro da borda: parte do mapa que está sendo exibida

def main():
    # Limpeza da tela
    wc.clrscr()
    wc.setcursortype(0)

    # Impressão fixa
    ## Impressão fora da margem
    titulo = 'SafariCatch'
    alinhar_centro(titulo, 0)
    print(titulo)
    tempo = '{}'.format(180)
    alinhar_direita(tempo, 1)
    print(tempo)

    ## Impressão dentro da margem
    alinhar_add_margem_tela(2)
    mapa = carregar_mapa('mapa.txt')
    pos_mapa_atual = encontrar_mapa_atual(mapa)

    # Impressão dinâmica (atualmente placeholders)
    ## Inicialização do mapa e do jogador
    att_container(mapa, 4)
    impressao_matriz_m(mapa, True, 2)
    origem_jogador(11, 3, 2)

    ## Animação de movimento para baixo
    sleep(0.4)
    movimentar_jogador(mapa[4][1], 0, 1, 2)
    sleep(0.4)
    movimentar_jogador(mapa[4][1], 0, 1, 2)

    # Iniciar timer e captura de movimento
    ## chamar timer

    ## movimento
    while(True):
        
        if wc.kbhit():
            _, key = wc.getch()

            if key == "w":  # move para cima
                movimentar_jogador(mapa[4][1], 0, -1, 0)
            elif key == "s":  # move para baixo
                movimentar_jogador(mapa[4][1], 0, 1, 2)
            elif key == "a":  # move para esquerda
                movimentar_jogador(mapa[4][1], -1, 0, 1)
            elif key == "d":  # move apra direita
                movimentar_jogador(mapa[4][1], 1, 0, 3)
            elif key == "q":  # sai do jogo
                break

    pass

if __name__ == "__main__":
    main()
