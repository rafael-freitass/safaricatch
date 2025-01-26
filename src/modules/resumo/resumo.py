# Importações de biblioteca
import WConio2 as wc
import sys
import os
from time import sleep

## Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))

# Importações do projeto
from utils.text_functions import *
from modules.score import score
from modules.jogador import movimento
from modules.combat import combat
from saves import gamestate

def main():
    texto_fim = 'Sua visita ao Safari acabou, veja seus resultados e volte sempre!'
    instrucao = 'Pressione enter para inciar um novo jogo ou qualquer tecla para voltar ao menu.'
    pontos = 'SCORE: {}'.format(score.obter_score_atual())
    passos = 'Passos dados: {}'.format(movimento.get_passos())
    encontros = 'Pokemons encontrados: {}'.format(combat.get_encontros())
    n_capturas = 'Pokemons capturados: {}'.format(combat.get_ncapturas())
    descobertas = 'Novos pokemons descobertos: {}'.format(combat.get_descobertas())

    
    wc.clrscr()
    wc.setcursortype(0)
    impressao_matriz(container_retangulo(31, 110), 10)
    alinhar_centro(texto_fim, 12)
    print(texto_fim)

    # Impressões com animação de escrita
    wc.setcursortype(2)
    for i in range(len(pontos)):
        wc.gotoxy(58 + i, 15)
        sleep(0.2)
        wc.putch(pontos[i])
    for i in range(len(passos)):
        wc.gotoxy(15 + i, 26)
        sleep(0.06)
        wc.putch(passos[i])
    for i in range(len(encontros)):
        wc.gotoxy(15 + i, 27)
        sleep(0.05)
        wc.putch(encontros[i])
    for i in range(len(n_capturas)):
        wc.gotoxy(15 + i, 28)
        sleep(0.05)
        wc.putch(n_capturas[i])
    for i in range(len(descobertas)):
        wc.gotoxy(15 + i, 29)
        sleep(0.03)
        wc.putch(descobertas[i])    
    wc.setcursortype(0)  

    # Salva a pontuação
    score.escrever_resume(pontos,passos,encontros,n_capturas,descobertas)

    # Reseta globais para a próxima partida
    gamestate.reset()
    movimento.reset_passos()
    score.reset_score()

    # Impressão normal
    alinhar_centro(instrucao, 38)
    print(instrucao)
    while True:
        if wc.kbhit():
            sleep(0.5)
            break



if __name__ == '__main__':
    main()
