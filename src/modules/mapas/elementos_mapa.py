# Importações
import WConio2

# Imprime o elemento e retorna à cor padrão
def imprimir_elemento(elemento: tuple, cor_padrao = 15, *pos_set: int):
    WConio2.textcolor(elemento[1])
    if (type(elemento[0]) == str):
        print(elemento[0], end='')
    else:
        print(elemento[0][pos_set[0]], end='')
    WConio2.textcolor(cor_padrao)


# Definições dos elementos de mapa no padrão:
#(caracter ou set de caracteres, cor WConio2)
def main():
    # Indicador do jogador
    jogador = (['▲', '◄', '▼', '►'], 13)

    # Elementos atravessáveis
    ## Terrenos
    vazio = (' ', 15) 
    água = ('≈', 11) 
    mato_alto = ('Ж', 2) 
    mato_baixo = ('ж', 10) 
    areia = ('₪', 14) 

    ## Elementos com eventos
    porta = ('∩', 15) 
    portal = ('۞', 15) 


    # Elementos intransponíveis
    ## Limites
    parede = ('▓', 4) 
    cerca = (['═', '║', '╔', '╗'], 4) 

    ## Elementos visuais de área
    ## Cemitério -> área de vazio com lápides
    ## Caverna -> área de vazio com pedras
    ## Floresta -> área de vazio com árvores
    lapide = ('†', 7) 
    pedra = ('⌂', 8) 
    arvore = ('♣', 10) 


if __name__ == '__main__':
    main()

