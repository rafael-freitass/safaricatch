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

def escrever_resume():
    with open("src/saves/resume.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Pontos totais: {pontos_totais}\n")
