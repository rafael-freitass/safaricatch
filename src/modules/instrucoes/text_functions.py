# Importações de biblioteca
import sys
import os
import re

# Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))

# Importações do projeto
from regex import palavra, silaba, pontuacao
from main import a, b   # @todo mudar essa importação quando alguma página definir o tamanho da matriz

# Globais
_tamanho_mod_ = [a, b]
_TAMANHO_ = tuple(_tamanho_mod_)

# Funções de formatação de texto
## Retorna altura e largura "livres" de um container regular
def calcular_capacidade(matriz):
    bordas_a = 0
    bordas_l = 0
    control = True
    for i in range(len(matriz)):
        if (matriz[i].count(' ') == 0):
                bordas_a += 1        
        else:
            if (control):
                for j in range(len(matriz[i])): 
                    if(not(matriz[i][j] == ' ')):
                        bordas_l += 1

            control = False

    altura = len(matriz) - bordas_a
    largura = len(matriz[0]) - bordas_l
    capacidade = [altura, largura]
    
    return capacidade

## Retorna True se a string passada é maior que o tamanho da matriz
def verificar_str_maior(string):
    global _tamanho_mod_
    if (len(string) <= _tamanho_mod_[1]):
        return False
    
    return True

## Retorna uma lista de strings, separador: última sílaba cabível
def separar_silaba(string):
    global _tamanho_mod_
    if (verificar_str_maior(string)):
        # Encontra posição do último espaço entre tamanho mínimo e máximo
        ultimo_espaco = string.rfind(' ', 0, _tamanho_mod_[1])
        if (ultimo_espaco == -1):
            ultimo_espaco = 0

        # Encontra e armazena a palavra completa após o espaço
        aux = re.match(palavra, string[ultimo_espaco:])
        ultima_palavra = aux.string[(aux.start()+1):aux.end()]
        if (ultima_palavra.startswith(' ')):
            ultima_palavra = ultima_palavra[1:]
        
        # Encontra a última sílaba da palavra antes de tamanho máximo
        pos = [len(string[:ultimo_espaco]), 0]
        while (True):
            aux = re.match(silaba, ultima_palavra[pos[1]:])
            if ((pos[0] + aux.end())< (_tamanho_mod_[1] - 1)):
                ultima_silaba = aux.string[aux.start():aux.end()]
                for i in range(len(pos)):
                    pos[i] += len(ultima_silaba)
            else:
                break

        # Cria a lista e separa a string pela última sílaba
        string_mod = [string[:(pos[0]+1)], string[(pos[0]+1):]]
        if (not(re.match(pontuacao, ultima_palavra) == None)):
            string_mod[0] = string_mod[0] + '-'
        return string_mod
    return ([string])

## Diminui espaço para escrita na tela, reseta margem anterior
def alinhar_add_margem_tela(integer):
    global _tamanho_mod_, _TAMANHO_

    if (integer < (_TAMANHO_[0]/2) and integer < (_TAMANHO_[1]/2)):
        for i in range(len(_TAMANHO_)):
            _tamanho_mod_[i] = _TAMANHO_[i] - (2*integer)
    return

## Alinha no centro com base no tamanho total
def alinhar_centro(string):
    global _TAMANHO_
    string.center(_TAMANHO_[1])
    pass

## Alinha à margem esquerda
def alinhar_esquerda(string):
    global _tamanho_mod_
    string.ljust(_tamanho_mod_[1])
    pass

## Alinha à margem direita
def alinhar_direita(string):
    global _tamanho_mod_
    string.rjust(_tamanho_mod_[1])
    pass

## Retorna uma lista de strings com mesmo tamanho 
def alinhar_justificar(lista_strings):
    global _tamanho_mod_
    maior_frase = len(max(lista_strings, key=len))
    pos_espacos = []
    for i in range(len(lista_strings)):
        # Encontra as posições de cada espaço nas frases menores
        if len(lista_strings[i]) < maior_frase:
            for j in range(len(lista_strings[i])):
                if lista_strings[i][j] == ' ':
                    pos_espacos.append(j)

            # Insere os espaços igualmente se for divisão exata
            if ((maior_frase - len(lista_strings[i])) % len(pos_espacos) == 0):
                divisor = int((maior_frase - len(lista_strings[i])) / len(pos_espacos))
                for e in range(len(pos_espacos), 0, -1):
                    lista_strings[i] = (lista_strings[i][:pos_espacos[e-1]+1] 
                                + (' ' * divisor) + lista_strings[i][pos_espacos[e-1]+1:])
            
            # Insere os espaços antes e depois da maior palavra em divisões não exatas
            else:
                diferenca = maior_frase - len(lista_strings[i])
                metade_dif = int(diferenca/2)
                palavras = re.findall(palavra, lista_strings[i])
                maior_palavra = max(palavras, key=len)
                start_maior_p = lista_strings[i].find(f'{maior_palavra}')
                end_maior_p = start_maior_p + len(maior_palavra)

                # Caso seja a primeira palavra, insere todos espaços depois
                if (start_maior_p == 0):
                    lista_strings[i] = lista_strings[i][:end_maior_p] + (' ' * diferenca) + lista_strings[i][end_maior_p:]
                else:
                    lista_strings[i] = (lista_strings[i][:start_maior_p] + (' ' * metade_dif)
                                + lista_strings[i][start_maior_p:end_maior_p] + (' ' * metade_dif) 
                                + lista_strings[i][end_maior_p:])
            
            # Verifica se realmente tem o mesmo tamanho
            if (not(len(lista_strings[i]) == maior_frase)):
                lista_strings[i] = lista_strings[i] + ' '

        else:
            lista_strings[i] = lista_strings[i]
    return lista_strings


# Funções de geração da tela
## Retorna uma matriz geradora de um retângulo com as dimensões passadas
def container_retangulo(altura, largura):
    m = []
    for i in range(altura):
        m.append([])
        for j in range(largura):
            # Caracteres da primeira linha
            if (i == 0):
                if (j == 0):
                    m[i].append('╒')
                elif (j == largura-1):
                    m[i].append('╕')
                else:
                    m[i].append('═')

            # Caracteres da última linha
            elif (i == altura-1):
                if (j == 0):
                    m[i].append('╘')
                elif (j == largura-1):
                    m[i].append('╛')
                else:
                    m[i].append('═')

            # Caracteres de preenchimento
            else:
                if (j == 0):
                    m[i].append('│')
                elif (j == largura-1):
                    m[i].append('│')
                else: 
                    m[i].append(' ')
    return m

## Insere texto em um container existente
def container_text(matriz_container, string):
    # Armazena valor original de _tamanho_mod e redefine
    global _tamanho_mod_
    backup_tamanho = _tamanho_mod_
    _tamanho_mod_ = calcular_capacidade(matriz_container)
    
    # Inicialização das variáveis de controle
    lista_string = separar_silaba(string)
    i = 1
    s = 0
    
    # Laço transcrevendo no container
    while i < len(lista_string):
        lista_string = lista_string[:i] + separar_silaba(lista_string[i])
        l = 0
        
        for j in range(len(matriz_container[i])):
            if (matriz_container[i][j] == ' '):
                if (l < len(lista_string[s])):
                    matriz_container[i][j] = lista_string[s][l]
                    l += 1
        s += 1
        i += 1
    # Repetição perdida pela inicialização fora do laço
    l = 0
    for j in range(len(matriz_container[i])):
            if (matriz_container[i][j] == ' '):
                if (l < len(lista_string[s])):
                    matriz_container[i][j] = lista_string[s][l]
                    l += 1
            
    # Redefine _tamanho_mod_ para o valor inicial
    _tamanho_mod_ = backup_tamanho

    return matriz_container

## Imprime matriz
def impressao_matriz(matriz):
    pass

## Imprime toda a tela
def impressao_tela(margem, alinhamento, matriz, init):
    alinhar_add_margem_tela(margem)
    
    match alinhamento:
        case 'c'|'centro'|'center'|'centralizar'|'centralizado':
            alinhar_centro(matriz)
        case 'd'|'direita'|'r'|'right':
            alinhar_direita(matriz)
        case 'e'|'esquerda'|'l'|'left':
            alinhar_esquerda(matriz)
        case 'j'|'justificar'|'justify'|'justificado':
            alinhar_justificar(matriz)
        case _:
            pass

    # @todo tem que imprimir a tela inteira, exceto a matriz, dps a matriz
    for i in range(_TAMANHO_[0]):
        if (i == init):
            print(matriz[i][j])
        for j in range(_TAMANHO_[1]):
                pass
        
# Testes
if __name__ == "__main__":
    pass