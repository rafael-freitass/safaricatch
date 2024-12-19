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

# Verifica se próximo char não é l nem n
n_ln = re.compile(r'(?![lnLN])')

# Compila consoantes e verificação de vogal
consoantes_pnv = re.compile(r'('+ consoantes_plural.pattern + n_vogal.pattern +r')')
consoantes_fnv = re.compile(r'('+ consoantes_finais.pattern + n_vogal.pattern +r')')

# Expressão que define sílabas
## padrões: vogal; consoante + vogal
## inicia mais específico vai até mais geral, devido operador | exclusivo
silaba = re.compile(
    r'(' # Primeira parte da sílaba 
    # encontros consonantais ou
    + consoantes_inseparaveis.pattern + r'|' 
    # consoantes solo (exceto ç) ou ç ou
    + todas_consoantes.pattern + r'|[çÇ]|'
    # vogais solo
    + todas_vogais.pattern + r')'

    r'(' # Segunda parte da sílaba
    # tritongo com consoante opcional que estende o som ou
    + r'(u'+ vogais_nu.pattern + semivogais.pattern + consoantes_pnv.pattern +r'?)|('
    # ditongo não-iniciado em u com plural opcional ou
    + vogais_nu.pattern + r'('+ semivogais.pattern + n_ln.pattern + r')([mrsMRS]'+ n_vogal.pattern + r')?)|'
    # ditongo(opcional) vogal com consoante opcional que estende o som ou
    + r'(u?'+ vogais_nu.pattern + consoantes_fnv.pattern +r'?)|('
    # consoantes 
    + consoantes_fnv.pattern + r'))', 
    flags=re.VERBOSE) 


