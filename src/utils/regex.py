import re

# Expressões regulares de formação de sílabas em PT-BR
# Expressões de vogais
todas_vogais = re.compile(r'[aà-ãeéêiíoóõuúAÀ-ÃEÊÉIÍOÓÕUÚ]')
vogais_nu = re.compile(r'[aà-ãeéêiíoóõAÀ-ÃEÊÉIÍOÓÕ]')
semivogais = re.compile(r'[eiouEIOU]')

# Expressões de consoantes
todas_consoantes = re.compile(r'[^aeiouAEIOU\W]')
consoantes_inseparaveis = re.compile(
    r'(([bcdfgptvBCDFGPTV][rlRL])|([cClLnN][hH])|([pP][nN]))')
consoantes_plural = re.compile(r'[mnsMNS]')
consoantes_finais = re.compile(r'[lmnrsLMNRS]')

# Verifica se próximo char não é uma vogal
n_vogal = re.compile(r'(?!'+ todas_vogais.pattern +r')')

# Verifica se próximo char não é l ou n
n_ln = re.compile(r'(?![lnLN])')

# Compila consoantes e verificação de vogal
consoantes_pnv = re.compile(r'('+ consoantes_plural + n_vogal +r')')
consoantes_fnv = re.compile(r'('+ consoantes_finais + n_vogal +r')')

# Expressão que define sílabas
## padrões: vogal; consoante + vogal
## parte do mais específico até o mais geral, 
## operador | exclusivo
silaba = re.compile(
    r'('+ consoantes_inseparaveis.pattern +r'|'
    + todas_consoantes.pattern +r'|'+ todas_vogais +r'|ç)('
    r'(u'+ vogais_nu.pattern + semivogais.pattern + consoantes_pnv.pattern +r')|'
    ++r')'
) 
## @todo transcrever ditongos em diante, revisar documentação
