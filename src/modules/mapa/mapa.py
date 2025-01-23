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

def main():
    # Limpeza da tela
    wc.clrscr()
    wc.setcursortype(0)

    # Impressão fixa
    ## Impressão fora da margem
    titulo = 'SafariCatch'
    score = 0
    tempo = '01:30'
    alinhar_centro(titulo, 0)
    print(titulo)
    alinhar_esquerda(1)
    print(f'SCORE: {score}')
    alinhar_direita(tempo, 1)
    print(f'{tempo}')

    ## Impressão dentro da margem
    ### Define o tamanho max para impressão do mapa
    alinhar_add_margem_tela(2)
    ### Chama o mapa com margem setada
    mapa = carregar_mapa('mapa.txt')
    ### Reseta a margem
    alinhar_add_margem_tela(0)

    ## Inicialização do mapa e do jogador
    impressao_matriz_m(mapa, True, 2)
    pos_mapa_atual = encontrar_mapa_atual(mapa)
    portais = encontrar_coord_portais(mapa)
    origem_jogador(75, 3, 2)
    ## Animação de surgimento/início do jogador
    sleep(0.4)
    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2)
    sleep(0.4)
    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2)

    # Iniciar timer, captura de movimento e reimpressões
    timer_Main()
    count = 0

    while(True):
        # Verifica repetições antes de reimprimir timer
        if (count%800 ==0):
            tempo = '{}'.format(segundo_Para_Minuto(num.value))
            alinhar_direita(tempo, 1)
            print(tempo)

        # Verifica se o tempo não acabou
        if(get_NumValue() == 0):
            terminar_Timer()
            chamar_menu()

        # Continuamente captura tecla
        if wc.kbhit():
            _, key = wc.getch()

            if key == "w":  # move para cima
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, -1, 0, portais, 2, mapa)
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                    

            elif key == "s":  # move para baixo
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2, portais, 2, mapa)
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                    

            elif key == "a":  # move para esquerda
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                # Verifica e atualiza mapa atual
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                # Movimenta o jogador
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], -1, 0, 1, portais, 2, mapa)
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                    
            elif key == "d":  # move apra direita
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 1, 0, 3, portais, 2, mapa)
                    pos_mapa_atual = encontrar_mapa_atual(mapa)

            elif key == "q":  # sai do jogo
                terminar_Timer()
                sleep(1)
                chamar_menu()

        count += 1

if __name__ == "__main__":
    main()
