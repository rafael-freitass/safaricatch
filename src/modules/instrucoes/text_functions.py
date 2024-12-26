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

# Funções de formatação
## Verifica se a string passada é maior que o tamanho da matriz
def verificar_str_maior(string):
    if (len(string) <= _tamanho_mod_[1]):
        return False
    
    return True

## Retorna uma lista de strings, separador: última sílaba cabível
def separar_silaba(string):
    if (verificar_str_maior(string)):
        # Encontra posição do último espaço entre tamanho mínimo e máximo
        ultimo_espaco = string.rfind(" ", 0, _tamanho_mod_[1])
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
            string_mod[0] = string_mod[0] + "-"
        return string_mod
    return ([string])

## Diminui espaço para escrita, reseta margem anterior
def alinhar_add_margem(integer):
    if (integer < (_TAMANHO_[0]/2) and integer < (_TAMANHO_[1]/2)):
        for i in range(len(_TAMANHO_)):
            _tamanho_mod_[i] = _TAMANHO_[i] - (2*integer)
    return

## Alinha no centro com base no tamanho total
def alinhar_centro(string):
    string.center(_TAMANHO_[1])
    pass

## Alinha à margem esquerda
def alinhar_esquerda(string):
    string.ljust(_tamanho_mod_[1])
    pass

## Alinha à margem direita
def alinhar_direita(string):
    string.rjust(_tamanho_mod_[1])
    pass

## Adiciona espaços para normalizar o tamanho de cada linha
def alinhar_justificar(lista_strings):
    maior = max(lista_strings, key=len)
    pos_espaços = []
    
    # Iguala espaços com a frase mais longa
    for i in range(len(lista_strings)):
        if len(lista_strings[i]) < maior:
            for j in range(len(lista_strings[i])):
                if lista_strings[i][j] == ' ':
                    pos_espaços.append(j)
            if ((len(pos_espaços) % (maior - len(lista_strings[i]))) == 0):
                pass
            
    pass

# Funções de geração da tela


# Testes
if __name__ == "__main__":
    _tamanho_mod_[0] = 5
    _tamanho_mod_[1] = 7
    separar_silaba("Abacate maduro") 
