# Importações
import WConio2

# Imprime o elemento e retorna à cor padrão 
# se for um elemento com set, necessário informar posição 
def imprimir_elemento(nome_elemento: str, cor_padrao = 15, pos_set = 0):
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
    print(char, end='')
    WConio2.textcolor(cor_padrao)

# Retorna um array de definições dos elementos ASCII de mapa no padrão
# {nome do elemento, caracter ou set de caracteres, cor WConio2}
def elementos_ASCII():
    # Indicador do jogador
    j = dict(nome='jogador', char=['^', '<', 'v', '>'], cor= 13)

    # Elementos atravessáveis
    ## Terrenos
    a1 = dict(nome='vazio', char=' ', cor= 15)
    a2 = dict(nome='agua', char='~', cor= 11)
    a3 = dict(nome='mato_alto', char='M', cor= 2)
    a4 = dict(nome='mato_baixo', char='m', cor= 10)
    a5 = dict(nome='areia', char='*', cor= 6)
 
    ## Elementos com eventos
    a6 = dict(nome='porta', char='A', cor= 15)
    a7 = dict(nome='portal', char='O', cor= 15)


    # Elementos intransponíveis
    ## Limites
    i1 = dict(nome='parede', char='%', cor= 4)
    i2 = dict(nome='cerca', char=['_', '|'], cor= 4)

    ## Elementos visuais de área
    ## Cemitério -> área de vazio com lápides
    ## Caverna -> área de vazio com pedras
    ## Floresta -> área de vazio com árvores
    i3 = dict(nome='lapide', char='+', cor= 7)
    i4 = dict(nome='pedra', char=',', cor= 8)
    i5 = dict(nome='arvore', char='T', cor= 10)

    elementos = [j, a1, a2, a3, a4, a5, a6, a7, i1, i2, i3, i4, i5]
    return elementos
