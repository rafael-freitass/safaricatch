pontos_totais = 0

def reset_score():
    global pontos_totais
    pontos_totais = 0

def aumentar_score(pokemon_pontos):
    global pontos_totais
    pontos_totais += pokemon_pontos
    return pontos_totais

def obter_score_atual():
    return pontos_totais

def escrever_resume(pontos,passos,encontros,n_capturas,descobertas):
    with open("src/saves/resume.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{pontos}\n{passos}\n{encontros}\n{n_capturas}\n{descobertas}\n")
