
# Importações de bibliotecas
import os
import sys
import WConio2 as wc
from time import sleep
import json

# Adição de caminhos
## Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))

## Adiciona caminho para 'jogador' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'jogador')))
## Adiciona caminho para 'jogador' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'resumo')))


# Importações do projeto
from modules.mapa import map_functions
from utils.timer import *
from utils.text_functions import *
from modules.jogador import movimento
from modules.resumo import resumo

def main():
    # Limpeza da tela
    wc.clrscr()
    wc.setcursortype(0)

    # Impressão fixa
    titulo = 'SafariCatch'
    score = 0
    tempo = '01:30'
    alinhar_centro(titulo, 0)
    print(titulo)
    alinhar_esquerda(1)
    print(f'SCORE: {score}')
    alinhar_direita(tempo, 1)
    print(f'{tempo}')

    # Impressão dentro da margem
    alinhar_add_margem_tela(2)
    mapa = map_functions.carregar_mapa('mapa.txt')
    alinhar_add_margem_tela(0)

    # Inicialização do mapa e do jogador
    impressao_matriz_m(mapa, True, 2)
    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)
    portais = map_functions.encontrar_coord_portais(mapa)
    movimento.origem_jogador(75, 3, 2)
    sleep(0.4)
    movimento.movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2)
    sleep(0.4)
    movimento.movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2)

    # Iniciar timer
    set_NumValue(30)
    count = 0

    while(True):
        # Verifica repetições antes de reimprimir timer
        if (count % 800 == 0):
            tempo = '{}'.format(segundo_Para_Minuto(num.value))
            alinhar_direita(tempo, 1)
            print(tempo)


        # Verifica se o tempo não acabou
        if get_NumValue() == 0:
            terminar_Timer()
            resumo.main()
            break 

        # Continuamente captura tecla
        if wc.kbhit():
            _, key = wc.getch()

            if key == "w":  # move para cima
                limite = movimento.verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (movimento.transicao_mapa(mapa, pos_mapa_atual, limite, map_functions.encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)
                else:
                    movimento.movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, -1, 0, portais, 2, pos_mapa_atual, mapa)
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)

            elif key == "s":  # move para baixo
                limite = movimento.verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (movimento.transicao_mapa(mapa, pos_mapa_atual, limite, map_functions.encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)
                else:
                    movimento.movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2, portais, 2, pos_mapa_atual, mapa)
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)

            elif key == "a":  # move para esquerda
                limite = movimento.verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (movimento.transicao_mapa(mapa, pos_mapa_atual, limite, map_functions.encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)
                else:
                    movimento.movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], -1, 0, 1, portais, 2, pos_mapa_atual, mapa)
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)

            elif key == "d":  # move para direita
                limite = movimento.verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (movimento.transicao_mapa(mapa, pos_mapa_atual, limite, map_functions.encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)
                else:
                    movimento.movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 1, 0, 3, portais, 2, pos_mapa_atual, mapa)
                    pos_mapa_atual = map_functions.encontrar_mapa_atual(mapa)

            elif key == "q":  # sai do jogo
                terminar_Timer()
                break

        count += 1

if __name__ == "__main__":
    main()

