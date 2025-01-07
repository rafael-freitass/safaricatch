# Importações do projeto
from text_functions import *
#@todo import controles
#@todo import timer

# Geração tela
title = 'INSTRUÇÕES'
mov_direita = 'D'
mov_esquerda = 'A'
mov_cima = 'W'
mov_baixo = 'S'
interagir = 'ESPAÇO'
proximo = 'qualquer tecla'
sair = 'ESC'
timer = 90
instrucaojogo = 'Você terá {} segundos para andar pelo mapa, usando {}, {}, {} e {} para passar por diferentes terrenos em busca de Pokemóns. Ao encontrar, aperte {} para tentar capturar! Caso você falhe, não se preocupe, há outros Pokemons à sua espera enquanto o tempo não acabar!'.format(timer, mov_cima, mov_esquerda, mov_baixo, mov_direita, interagir)
instrucaomenu = 'Para selecionar opções do menu, utilize as teclas {} e {} para navegar e pressione {} para escolher a opção. Para retornar à etapa anterior, pressione {}. Caso um texto ou tela continue, o que é indicado por "..." pressione {} para ver o restante.'.format(mov_cima, mov_baixo, interagir, sair, proximo)

tela = comb_container(
            [alinhar_centro(title)],
            tecla_com_label(mov_cima, 'Mover para cima'),
            tecla_com_label(mov_esquerda, 'Mover para esquerda'),
            tecla_com_label(mov_direita, 'Mover para direita'),
            tecla_com_label(mov_baixo, 'Mover para baixo'),
            tecla_com_label(interagir, 'Interagir'),
            tecla_com_label(proximo, 'Continuar'),
            tecla_com_label(sair, 'Retornar'),
            container_text(container_textbox(20, 30), instrucaojogo),
            container_text(container_textbox(7, 40), instrucaomenu))

impressao_matriz(tela)
#@todo corte de página por limite e atualização (funções já implementadas, testagem e ajuste)

#@todo alinhamentos
# titulo; centralizado
# caixa: controles: tecla, texto; 1 por linha, centralizado
# texto com instruções justificado

# Testes
if __name__ == "__main__":
    pass