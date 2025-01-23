# Importações
import WConio2

# Imprime o elemento e retorna à cor padrão 
# se for um elemento com set, necessário informar posição 
def imprimir_elemento(nome_elemento: str, pos_set = 0, cor_padrao = WConio2.WHITE):

    elementos = elementos_ASCII()

    # Busca elemento e cor segundo nome
    for i in range(len(elementos)):
        if (elementos[i].get('nome') == nome_elemento):
            # Verifica se o char é único ou é um set
            if (type(elementos[i].get('char')) == str):
                char = elementos[i].get('char')
                cor = elementos[i].get('cor')
                break
            else:
                char = elementos[i].get('char')[pos_set]
                cor = elementos[i].get('cor')
                break

    WConio2.textcolor(cor)
    WConio2.putch(char)
    WConio2.textcolor(cor_padrao)

# Retorna um array de definições dos elementos ASCII de mapa no padrão
# {nome do elemento, caracter ou set de caracteres, cor WConio2}
def elementos_ASCII():
    # Indicador do jogador
    j = dict(nome='jogador', char=['^', '<', 'v', '>'], cor= WConio2.LIGHTMAGENTA)

    # Elementos atravessáveis
    ## Terrenos
    a1 = dict(nome='vazio', char=' ', cor= WConio2.WHITE)
    a2 = dict(nome='agua', char='~', cor= WConio2.LIGHTBLUE)
    a3 = dict(nome='mato_alto', char='M', cor= WConio2.GREEN)
    a4 = dict(nome='mato_baixo', char='m', cor= WConio2.LIGHTGREEN)
    a5 = dict(nome='areia', char='*', cor= WConio2.BROWN)
    ## Elementos com eventos
    a6 = dict(nome='porta', char='A', cor= WConio2.WHITE)
    a7 = dict(nome='portal', char='O', cor= WConio2.WHITE)


    # Elementos intransponíveis
    ## Limites
    i1 = dict(nome='parede', char='%', cor= WConio2.RED)
    i2 = dict(nome='cerca', char=['_', '|'], cor= WConio2.RED)

    ## Elementos visuais de área
    ## Cemitério -> área de vazio com lápides
    ## Caverna -> área de vazio com pedras
    ## Floresta -> área de vazio com árvores
    i3 = dict(nome='lapide', char='+', cor= WConio2.DARKGRAY)
    i4 = dict(nome='pedra', char=',', cor= WConio2.LIGHTGRAY)
    i5 = dict(nome='arvore', char='T', cor= WConio2.LIGHTGREEN)

    elementos = [j, a1, a2, a3, a4, a5, a6, a7, i1, i2, i3, i4, i5]
    return elementos
