# Funções úteis para a criação da tela de mapa

# Importações de bibliotecas
import os
import sys
import WConio2 as wc

# Adição de caminhos
## Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))

## Adiciona caminho para 'menu' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'menu')))


# Importações do projeto
from modules.mapa import elementos_mapa
from utils.text_functions import *
from menu import main as menu_main

# Funções de manipulação de mapa
## Retorna o mapa como uma lista de matrizes do tamanho da tela
def carregar_mapa(nome_arquivo_mapa: str):
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), nome_arquivo_mapa))) as arquivo:
        mapa = arquivo.read().split('\n')
        return (divide_content(mapa, True))
        
## Retorna coordenadas (4d) de todas ocorrências de portal no mapa
def encontrar_coord_portais(mapa: list):
    elementos = elementos_mapa.elementos_ASCII() 

    # Busca char definido como portal
    for i in range(len(elementos)):
        if (elementos[i].get('nome') == 'portal'):
                portal = elementos[i].get('char')
                break

    coordenadas = []

    # Itera lista de matrizes
    for i in range(len(mapa)):
        if type(mapa[i][1]) == list:
            # Itera cada matriz
            for j in range(len(mapa[i][1])):
                # Itera cada linha
                for k in range(len(mapa[i][1][j])):
                    if (mapa[i][1][j][k] == portal):
                        coordenadas.append([i, 1, k, j])

    return coordenadas    

## Retorna coordenadas (2d) do mapa atualmente sendo exibido
def encontrar_mapa_atual(mapa: list):
    # Itera a lista de matrizes
    for i in range(len(mapa)):
        # Para de iterar ao encontrar mapa atual
        if (mapa[i][0]):
            return([i, 1])

## Retorna uma lista com posição (index) de todos separadores
def encontrar_todos_separadores(mapa: list):
    todos_separadores = []

    # Itera a lista de matrizes
    for i in range(len(mapa)):
        # Para de iterar ao encontrar separador
        if type(mapa[i][1]) == int:
            todos_separadores.append(i)

    return todos_separadores

## Retorna True se um próximo mapa existe, no sentido 
## x (horizontal) ou y (vertical), antes (-1) ou após (1) o mapa atual 
def verificar_transicao_mapa(mapa: list, pos_mapa_atual: list, x_ou_y: str, dir: int):
    pos_mapa_atual = encontrar_mapa_atual(mapa)
    separadores = encontrar_todos_separadores(mapa)
    intervalo_atual = []

    # Encontra o intervalo atual 
    if (pos_mapa_atual[0] < separadores[0]):
        intervalo_atual.append(0)
        intervalo_atual.append(separadores[0])
    elif (pos_mapa_atual[0] > separadores[-1]):
        intervalo_atual.append(separadores[-1])
        intervalo_atual.append((len(mapa)-1))
    else:
        for i in range(len(separadores)-1):
            if (separadores[i] < pos_mapa_atual[0] and separadores[i+1] > pos_mapa_atual[0]):
                intervalo_atual.append(separadores[i])
                intervalo_atual.append(separadores[i+1])
                break

    # Retorna True se entre o separador e o mapa atual há alguma matriz
    if x_ou_y == 'x':
        if dir == 1:
            for i in range(pos_mapa_atual[0], intervalo_atual[1]):
                return True
        elif dir == -1:
            for i in range(pos_mapa_atual[0], intervalo_atual[0], dir):
                return True
    
    # Retorna True se entre antes/após o separador há matrizes
    if x_ou_y == 'y':
        if dir == 1:
            if (intervalo_atual[1] == (len(mapa)-1)):
                return False
            for i in range((intervalo_atual[1] + 1), (len(mapa) - 1)):
                return True
        elif dir == -1:
            if intervalo_atual[0] == 0:
                return False
            for i in range((intervalo_atual[0] - 1), 0, dir):
                return True
    
    return False

# Funções de fluxo/importação
def chamar_menu():
    menu_main()

def pause_game():
    pass

def despause():
    pass