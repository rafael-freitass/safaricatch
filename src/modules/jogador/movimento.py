# Importações de biblioteca
import random
import WConio2 as wc
import os
import sys
import json
from time import sleep

# Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))

## Adiciona caminho para 'mapa' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'mapa')))

## Adiciona caminho para 'combat' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'combat')))

# Importações do projeto
from modules.mapa import elementos_mapa
from utils.text_functions import *
from utils.timer import *
from modules.score import score
from modules.combat import combat
from combat import main as combat_main


# Globais
_pos_xy_jogador_ = [1, 1]
_passos_ = 0
_CHANCE_POKEMON_ = 0.12
_pokeball_list_ = combat.carregar_pokebolas("src/saves/pokeballs.json")

def carregar_pokebolas(caminho): # abre o json com info das pokeballs 
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo pokeballs.json não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo pokeballs.json contém erros.")
        return []

# Retorna True se o elemento no mapa for passável, False se não for passável
def verificar_colisao(mapa_atual: list, pos_x: int, pos_y: int):
    elementos = elementos_mapa.elementos_ASCII()
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

# Retorna passos
def get_passos():
    global _passos_
    return _passos_

# Reseta passos
def reset_passos():
    global _passos_
    _passos_ = 0

# Retorna uma tupla se jogador está no limite do mapa
# no padrão (bool, 'x' ou 'y', 1 ou -1)
def verificar_limite(mapa_atual:list):
    global _pos_xy_jogador_

    limite_x = len(mapa_atual[0]) - 1
    limite_y = len(mapa_atual) - 1

    # Limites iniciais
    if (_pos_xy_jogador_[0] == 0):
        return tuple([True, 'x', -1])
    if (_pos_xy_jogador_[1] == 0):
        return tuple([True, 'y', -1])
    
    # Limites finais
    if (_pos_xy_jogador_[0] == limite_x):
        return tuple([True, 'x', 1])
    if (_pos_xy_jogador_[1] ==  limite_y):
        return tuple([True, 'y', 1]) 
    
    return tuple([False, 0, 0])

# Retorna True se teleportou, atualiza visualização e posição do jogador seguindo coordenadas 4d
def teleporte(mapa:list, coordenada_inicial:list, coordenada_final:list, direcao = 0, mod=0, borda=2):
    global _pos_xy_jogador_
    # usa o primeiro par para identificar se está numa matriz sendo exibida e segundo par para verificar posição do jogador é igual ao ponto de teleporte
    if ((mapa[coordenada_inicial[0]][0]) and (_pos_xy_jogador_ == [coordenada_inicial[2], coordenada_inicial[3]])):
        att_container(mapa, mod, coordenada_final[0])
        pause_Timer()
        wc.clrscr()
        titulo = 'SafariCatch'
        alinhar_centro(titulo, 0)
        print(titulo)
        alinhar_esquerda(1)
        print(f'SCORE: {score.obter_score_atual()}')
        impressao_matriz_m(mapa, True, borda)
        despause_Timer()
        origem_jogador(coordenada_final[2], coordenada_final[3], direcao, borda)
        return True
    elif ((mapa[coordenada_final[0]][0] == True) and (_pos_xy_jogador_ == [coordenada_final[2], coordenada_final[3]])):
        att_container(mapa, (mod*(-1)), coordenada_inicial[0])
        pause_Timer()
        wc.clrscr()
        titulo = 'SafariCatch'
        alinhar_centro(titulo, 0)
        print(titulo)
        alinhar_esquerda(1)
        print(f'SCORE: {score.obter_score_atual()}')
        impressao_matriz_m(mapa, True, borda)
        despause_Timer()
        origem_jogador(coordenada_inicial[2], coordenada_inicial[3], direcao, borda)
        return True
    return False

# Altera a global de posição e imprime jogador na posição passada
def origem_jogador(coord_x: int, coord_y: int, direcao = 0, borda_tela = 2):
    global _pos_xy_jogador_

    _pos_xy_jogador_[0] = coord_x
    _pos_xy_jogador_[1] = coord_y

    wc.gotoxy(coord_x + borda_tela, coord_y + borda_tela)
    elementos_mapa.imprimir_elemento_bn('jogador', 15, direcao)
    wc.gotoxy(0, 30)    

# Retorna boolean, caso trocou de mapa, verifica e troca de mapa caso jogador esteja no limite entre mapas 
def transicao_mapa(mapa: list, pos_mapa_atual: list, limite: tuple, separadores: list, key: str):
    if limite[0]:
        pos_inicial = [pos_mapa_atual[0], pos_mapa_atual[1], _pos_xy_jogador_[0], _pos_xy_jogador_[1]]

        if limite[1] == 'y' and limite[2] == -1 and key == 'w':
            pos_final = [(pos_inicial[0] - (separadores[0] + 1)), pos_inicial[1], _pos_xy_jogador_[0], (len(mapa[0][1]) -1)]
            teleporte(mapa, pos_inicial, pos_final, 0, -1)
            return True
        elif limite[1] == 'y'and limite[2] == 1 and key == 's':
            pos_final = [(pos_inicial[0] + (separadores[0] + 1)), pos_inicial[1], _pos_xy_jogador_[0], 0]
            teleporte(mapa, pos_inicial, pos_final, 2, 1)
            return True
        
        elif limite[1] == 'x' and limite[2] == -1 and key == 'a':
            pos_final = [pos_inicial[0] - 1, pos_inicial[1], (len(mapa[0][1][0])-1), _pos_xy_jogador_[1]]
            teleporte(mapa, pos_inicial, pos_final, 1, -1)
            return True
        
        elif limite[1] == 'x' and limite[2] == 1 and key == 'd':
            pos_final = [pos_inicial[0] + 1, pos_inicial[1], 0, _pos_xy_jogador_[1]]
            teleporte(mapa, pos_inicial, pos_final, 3, 1)
            return True

    return False

# Movimentação do jogador com verificações e impressão.
def movimentar_jogador(mapa_atual, mod_x, mod_y, posicao, portais= [], borda=2, pos_mapa_atual =[], *mapa):
    global _pos_xy_jogador_
    global _passos_
    
    novo_x = _pos_xy_jogador_[0] + mod_x
    novo_y = _pos_xy_jogador_[1] + mod_y
    achou = False

    # Verifica colisão com o mapa_atual antes de mover
    if (verificar_colisao(mapa_atual, novo_x, novo_y)):
        # Sobrepõe cursor antigo com elemento do mapa_atual
        wc.gotoxy(_pos_xy_jogador_[0] + borda, _pos_xy_jogador_[1] + borda)
        elementos_mapa.imprimir_elemento_bc(mapa_atual[_pos_xy_jogador_[1]][_pos_xy_jogador_[0]])
        
        # Atualiza posição do jogador
        _pos_xy_jogador_[0] = novo_x 
        _pos_xy_jogador_[1] = novo_y

        # Sobrepõe elemento do mapa_atual com jogador
        wc.gotoxy(_pos_xy_jogador_[0] + borda, _pos_xy_jogador_[1] + borda)
        elementos_mapa.imprimir_elemento_bn('jogador', 15, posicao)

        # Adiciona no contador de passos
        _passos_ += 1

        # Teleporta, se estiver em portal e ainda não tiver feito
        teleportou = False
        if not(len(mapa) == 0 and len(portais) == 0) and teleportou == False:
            teleportou = teleporte(mapa[0], portais[0], portais[2])
            
        if not(len(mapa) == 0 and len(portais) == 0) and teleportou == False:
            teleportou = teleporte(mapa[0], portais[1], portais[3])
        
        if teleportou == False and achou == False:
            # Gera chance de encontrar pokemon
            areas = elementos_mapa.areas_caca()
            for i in range(len(areas)):
                if (mapa_atual[_pos_xy_jogador_[1]][_pos_xy_jogador_[0]] == areas[i]) and random.random() < _CHANCE_POKEMON_:
                    alinhar_centro("Você encontrou um Pokémon! Pressione qualquer tecla para continuar.", 44)
                    wc.textcolor(wc.YELLOW)
                    print("Você encontrou um Pokémon! Pressione qualquer tecla para continuar.")
                    wc.getch()
                    wc.clrscr()
                    wc.textcolor(wc.WHITE)
                    pause_Timer()
                    combat.animacao_espiral(mapa_atual)
                    # Chama combate
                    combat_main(_pokeball_list_, pos_mapa_atual)
                    # Reimprime valor de score
                    titulo = 'SafariCatch'
                    alinhar_centro(titulo, 0)
                    print(titulo)
                    alinhar_esquerda(1)
                    print(f'SCORE: {score.obter_score_atual()}')
                    achou = True
                    break

