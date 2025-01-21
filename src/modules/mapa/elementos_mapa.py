# Importações
import WConio2

# Retorna um array de definições dos elementos ASCII de mapa no padrão
# {nome, char, cor, pass} *char pode ser um array ou str
def elementos_ASCII():
    # Indicador do jogador
    j = dict(nome='jogador', char=['^', '<', 'v', '>'], cor= WConio2.LIGHTMAGENTA, passa=True)

    # Elementos atravessáveis
    ## Terrenos
    a1 = dict(nome='vazio', char=' ', cor= WConio2.WHITE, passa=True)
    a2 = dict(nome='agua', char='~', cor= WConio2.LIGHTBLUE, passa=True)
    a3 = dict(nome='mato_alto', char='M', cor= WConio2.GREEN, passa=True)
    a4 = dict(nome='mato_baixo', char='m', cor= WConio2.LIGHTGREEN, passa=True)
    a5 = dict(nome='areia', char='*', cor= WConio2.BROWN, passa=True)
 
    ## Elementos com eventos
    a6 = dict(nome='porta', char='A', cor= WConio2.WHITE, passa=True)
    a7 = dict(nome='portal', char='O', cor= WConio2.WHITE, passa=True)
    a8 = dict(nome='escada', char='H', cor= WConio2.LIGHTGRAY, passa=True)


    # Elementos intransponíveis
    ## Limites
    i1 = dict(nome='parede', char='%', cor= WConio2.RED, passa= False)
    i2 = dict(nome='cerca', char=['_', '-', '|'], cor= WConio2.RED, passa= False)

    ## Elementos visuais de área
    ## Cemitério -> área de vazio com lápides
    ## Caverna -> área de vazio com pedras
    ## Floresta -> área de vazio com árvores
    i3 = dict(nome='lapide', char='+', cor= WConio2.DARKGRAY, passa= False)
    i4 = dict(nome='pedra', char=',', cor= WConio2.LIGHTGRAY, passa= False)
    i5 = dict(nome='arvore', char='T', cor= WConio2.LIGHTGREEN, passa= False)
    i6 = dict(nome='gelo', char='#', cor= WConio2.DARKGRAY, passa= False)

    elementos = [j, a1, a2, a3, a4, a5, a6, a7, a8, i1, i2, i3, i4, i5, i6]
    return elementos

# Imprime o elemento buscando pelo nome dele e retorna à cor padrão 
# se for um elemento com set, necessário informar posição 
def imprimir_elemento_bn(nome_elemento: str, cor_padrao = 15, pos_set = 0):
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

# Imprime o elemento buscando pelo char dele e retorna à cor padrão 
def imprimir_elemento_bc(char_elemento: str, cor_padrao = 15):
    elementos = elementos_ASCII()
    achou = False

    # Itera lista de elementos
    for i in range(len(elementos)):
        # Verifica se o char é único ou é um set
        if (type(elementos[i].get('char')) == str):
            if (elementos[i].get('char') == char_elemento):
                char = char_elemento
                cor = elementos[i].get('cor')
                break
        else:
            # Percorre o set de elementos para comparar
            for j in range(len(elementos[i].get('char'))):
                if(elementos[i].get('char')[j] == char_elemento):
                    char = char_elemento
                    cor = elementos[i].get('cor')
                    achou = True
                    break
            if (achou == True):
                break

    WConio2.textcolor(cor)
    WConio2.putch(char)
    WConio2.textcolor(cor_padrao)



