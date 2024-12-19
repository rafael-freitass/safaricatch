# Importações de biblioteca
import sys
import os
import re

# Adiciona caminho para 'utils' na busca de módulos
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utils')))

# Importações do projeto
import regex
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
        ultimo_espaco = string.rfind(" ", 0, _tamanho_mod_[1])
        if (ultimo_espaco == -1):
            ultimo_espaco = 0
        ultima_silaba = re.match(string[silaba, ultimo_espaco:_tamanho_mod_[1]]) 
        # @todo substituir esse método para um que retorne ultimo encontrado ou posição, ou ambos 
        for i in range (_tamanho_mod_[1], ultimo_espaco, (len(ultima_silaba)*-1)):
            
            if ( a == b):
                string_mod = [string[:string[i]] + "-", string[string[i]:]]
            break

        return string_mod
    return string

## Retorna uma lista de strings, separador: último espaço (' ') cabível
def separar_linha(string):
    pass

## Reseta margem, diminui espaço para escrita
def alinhar_add_margem(integer):
    if (integer < (_TAMANHO_[0]/2) and integer < (_TAMANHO_[1]/2)):
        for i in range(len(_TAMANHO_)):
            _tamanho_mod_[i] = _TAMANHO_[i] - 2*integer
    return

def alinhar_centro(string):
    string.center(_TAMANHO_[1])
    pass

def alinhar_esquerda(string):
    string.ljust(_tamanho_mod_[1])
    pass

def alinhar_direita(string):
    string.rjust(_tamanho_mod_[1])
    pass

def alinhar_justificar(lista_strings):
    maior = max(lista_strings, key=len)
    pos_espaços = []
    
    # Iguala espaços com a frase mais longa
    for i in range(len(lista_strings)):
        if len(i) < maior:
            for j in range(len(lista_strings[i])):
                if lista_strings[i][j] == ' ':
                    pos_espaços.append(j)
                
    pass

# Funções de geração da tela


# Testes
if __name__ == "__main__":
    _tamanho_mod_[0] = 5
    _tamanho_mod_[1] = 7
    separar_silaba("Aba maduro") 
