import WConio2 as wc
import cursor
import json, os, sys, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from modules.combat import combat
from modules.score import score
from modules.menu import menu
from utils.timer import timer
#Ainda precisa importar map_functions.py, mas eu não encontrei no código

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


pokeball_list = carregar_pokebolas("src/saves/pokeballs.json")

VAZIO = " "
PAREDE = "#"
NAVEGAVEL = "."
MATO = "M"
JOGADOR = "@"

maxI = 10  # Altura
maxJ = 20  # Largura
jogadorI, jogadorJ = 1, 1

CHANCE_POKEMON = 0.3


def inicializar_matriz(matriz):
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

def desenhar_tela(matriz):
    wc.gotoxy(0, 0)
    for i in range(maxI):
        for j in range(maxJ):
            if i == jogadorI and j == jogadorJ:
                wc.textcolor(wc.RED)  # Cor do jogador
                wc.putch(JOGADOR)
                wc.textcolor(wc.WHITE)
            elif matriz[i][j] == PAREDE:
                wc.textcolor(wc.DARKGRAY)  # Cor das paredes
                wc.putch(PAREDE)
                wc.textcolor(wc.WHITE)
            elif matriz[i][j] == NAVEGAVEL:
                wc.textcolor(wc.BROWN)  # Cor das áreas navegáveis
                wc.putch(NAVEGAVEL)
                wc.textcolor(wc.WHITE)
            elif matriz[i][j] == MATO:
                wc.textcolor(wc.GREEN)  # Cor do mato
                wc.putch(MATO)
                wc.textcolor(wc.WHITE)
        wc.putch("\n")

def movimentar_jogador(dI, dJ, matriz):
    global jogadorI, jogadorJ
    novoI, novoJ = jogadorI + dI, jogadorJ + dJ

    if matriz[novoI][novoJ] in [NAVEGAVEL, MATO]:
        jogadorI, jogadorJ = novoI, novoJ
        if matriz[novoI][novoJ] == MATO and random.random() < CHANCE_POKEMON:
            combat.animacao_espiral(matriz)
            combat.main(pokeball_list)

def rodar():
    matriz = []
    wc.clrscr()
    cursor.hide()
    inicializar_matriz(matriz)

    while True:
        desenhar_tela(matriz)
        print(f"score: {score.obter_score_atual()}")
        if wc.kbhit():
            _, key = wc.getch()

            if key == "w":  # move para cima
                movimentar_jogador(-1, 0, matriz)
            elif key == "s":  # move para baixo
                movimentar_jogador(1, 0, matriz)
            elif key == "a":  # move para esquerda
                movimentar_jogador(0, -1, matriz)
            elif key == "d":  # move apra direita
                movimentar_jogador(0, 1, matriz)
            elif key == "q":  # sai do jogo
                break

def chamar_sim():
    timer.set_NumValue(-3)
    menu.main()

def chamar_nao():
    map_functions.despause()

def opcao_sim():
    return {"SIM": chamar_sim()}

def opcao_nao():
    return {"NAO": chamar_nao()}

def carregar_opcoes_saida(sim, nao):
    return {
        """
|-----------------------------------------------------|
|             Gostaria de sair do jogo?               | 
|                        {}                        |
|                        {}                        |
|(Aviso caso irá perder o progresso e sobre falhar    |
| a captura do pokemon caso esteja em combate agora)  |
|-----------------------------------------------------|             
""".format(sim, nao)
}