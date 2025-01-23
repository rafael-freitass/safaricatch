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

_score_ = 0

def get_score():
    global _score_
    
    _score_ +=1
    return _score_


def main():
    # Limpeza da tela
    wc.clrscr()
    wc.setcursortype(0)

    # Impressão fixa
    ## Impressão fora da margem
    titulo = 'SafariCatch'
    score = 'Pontuação: {}'.format(0)
    tempo = '{}'.format('03:00')
    alinhar_centro(titulo, 0)
    print(titulo)
    alinhar_esquerda(score, 1)
    print(score)
    alinhar_direita(tempo, 1)
    print(tempo)

    ## Impressão dentro da margem
    ### Define o tamanho max para impressão do mapa
    alinhar_add_margem_tela(2)
    ### Chama o mapa com margem setada
    mapa = carregar_mapa('mapa.txt')
    ### Reseta a margem
    alinhar_add_margem_tela(0)
    
    pos_mapa_atual = encontrar_mapa_atual(mapa)
    
    # Impressão dinâmica (atualmente placeholders)
    ## Inicialização do mapa e do jogador
    impressao_matriz_m(mapa, True, 2)
    origem_jogador(75, 3, 2)

    ## Animação de surgimento/início do jogador
    sleep(0.4)
    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2)
    sleep(0.4)
    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2)

    # Iniciar timer e captura de movimento
    ## chamar timer
    timer_Main()

    ## movimento
    while(True):
        # Reimprime o tempo
        alinhar_direita(tempo, 1)
        tempo = '{}'.format(segundo_Para_Minuto(get_NumValue()))

        # Verifica se o tempo não acabou
        if(get_NumValue() == 0):
            terminar_Timer()
            chamar_menu()

        if wc.kbhit():
            _, key = wc.getch()

            if key == "w":  # move para cima
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, -1, 0)


            elif key == "s":  # move para baixo
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 0, 1, 2)

            elif key == "a":  # move para esquerda
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                # Verifica e atualiza mapa atual
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                # Movimenta o jogador
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], -1, 0, 1)

            elif key == "d":  # move apra direita
                # Atualiza variavel limite
                limite = verificar_limite(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]])
                if (transicao_mapa(mapa, pos_mapa_atual, limite, encontrar_todos_separadores(mapa), key)):
                    pos_mapa_atual = encontrar_mapa_atual(mapa)
                else:
                    movimentar_jogador(mapa[pos_mapa_atual[0]][pos_mapa_atual[1]], 1, 0, 3)
                    
            elif key == "q":  # sai do jogo
                terminar_Timer()
                chamar_menu()
        
        # Reimprime score
        score = 'Pontuação: {}'.format(get_score())
        alinhar_esquerda(score, 1)
        print(score)
        

if __name__ == "__main__":
    main()
